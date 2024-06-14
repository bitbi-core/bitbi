import subprocess
import os
import fileinput
import mimetypes
import shutil
import tarfile
import argparse

DEST_BITBI = '/home/buji/code/bitbi/bitbi'
SRC_BTC = '/home/buji/code/bitbi/btc-btb'

def create_release_branch():
    # Get the name of the current branch
    result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE, check=True)
    current_branch = result.stdout.decode('utf-8').strip()
    if current_branch.endswith('-release'):
        print('You are on the release branch, ignore to create a new one')
        #remove the release suffix
        current_branch = current_branch[:-8]
        return current_branch
    # Name of the new branch
    branch_name = f'{current_branch}-release'
    # Check if the branch already exists
    result = subprocess.run(['git', 'show-ref', '--verify', f'refs/heads/{branch_name}'], stdout=subprocess.PIPE)
    if result.returncode == 0:
        print(f'Branch {branch_name} already exists, checking it out')
        subprocess.run(['git', 'checkout', branch_name], check=True)
    else:
        print(f'Creating branch: {branch_name}')
        # Create the new branch
        subprocess.run(['git', 'checkout', '-b', branch_name], check=True)
    return current_branch


def replace_keywords():
    src_dir = '.'  # current directory

    for dirpath, dirnames, filenames in os.walk(src_dir):
        # Modify dirnames in-place to remove directories that start with '.'
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        ignored_dirs = ['depends', 'private-tools', 'node_modules', 'build', 'dist', 'venv', 'env', 'target', 'lib', 'libs', 'bin', 'include', 'obj', 'deps',  'tmp', 'temp', 'cache', 'data', 'media', 'assets', 
                        'images', 'img', 'fonts', 'css', 'scss', 'sass', 'less']
        dirnames[:] = [d for d in dirnames if d not in ignored_dirs]
        # Filter filenames to remove files that start with '.' 
        filenames = [f for f in filenames if not f.startswith('.') ]
        ignored_files = ['./src/kernel/chainparams.cpp']
        filenames = [f for f in filenames if os.path.join(dirpath, f) not in ignored_files]

        #ignore all the files and dirs in .gitignore file
        with open('.gitignore') as f:
            ignore_list = f.read().splitlines()
        dirnames[:] = [d for d in dirnames if d not in ignore_list]
        filenames = [f for f in filenames if f not in ignore_list]


        # Replace content in files
        for filename in filenames:
            ingored_suffix = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.woff', 
                              '.woff2', '.ttf', '.eot', '.otf','.o', '.a', '.so', '.pyc']
            if any(filename.endswith(suffix) for suffix in ingored_suffix):
                continue
            print(f'Processing file: {filename}')
            try:
                with fileinput.FileInput(os.path.join(dirpath, filename), inplace=True) as file:
                    for line in file:
                        new_line = line.replace('bitcoincore.org', 'bitbi.org').replace('bitcoin', 'bitbi').replace('Bitcoin', 'Bitbi').replace('BTC', 'BTB').replace('btc', 'btb')
                        print(new_line, end='')
            except UnicodeDecodeError:
                print(f'not text file: {filename}')
                continue
        # Rename files
        for filename in filenames:
            if 'bitcoin' in filename:
                new_name = filename.replace('bitcoin', 'bitbi')
                os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_name))

def delete_files_with_bitbi_in_name():
    src_dir = '.'  # current directory

    for dirpath, dirnames, filenames in os.walk(src_dir):
        # Modify dirnames in-place to remove directories that start with '.'
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        ignored_dirs = ['depends', 'private-tools', 'node_modules', 'build', 'dist', 'venv', 'env', 'target', 'lib', 'libs', 'bin', 'include', 'obj', 'deps',   'tmp', 'temp', 'cache', 'data', 'media', 'assets', 
                        'images', 'img', 'fonts', 'css', 'scss', 'sass', 'less']
        dirnames[:] = [d for d in dirnames if d not in ignored_dirs]
        # Filter filenames to remove files that start with '.' 
        filenames = [f for f in filenames if not f.startswith('.') ]

        #ignore all the files and dirs in .gitignore file
        with open('.gitignore') as f:
            ignore_list = f.read().splitlines()
        dirnames[:] = [d for d in dirnames if d not in ignore_list]
        filenames = [f for f in filenames if f not in ignore_list]

        # Replace content in files
        for filename in filenames:
            if 'bitbi' in filename:
                os.remove(os.path.join(dirpath, filename))

def git_reset_hard():
    subprocess.run(['git', 'reset', '--hard'], check=True)

def tar_gz_file(version: str):
    os.chdir(DEST_BITBI)
    #remove the dist/bin and recreate it
    os.system('rm -rf dist/bin')
    os.makedirs('dist/bin')
    bin_files = ['./src/bitbi-cli', './src/bitbi-tx', './src/bitbi-util', './src/bitbi-wallet', 
             './src/bitbid', './src/qt/bitbi-qt']
    #copy each file into dist/bin
    files_to_zip = []
    for file in bin_files:
        print(f'Copying file: {file}')
        filename = file.split('/')[-1]
        bin_file = f'dist/bin/{filename}'
        shutil.copy(file, bin_file)
        files_to_zip.append(bin_file)
    # Create a tar.gz file
    tar_gz_file = f'dist/bitbi-{version}-x86_64-linux-gnu.tar.gz'
    # delete the old tar.gz file
    os.system(f'rm -f {tar_gz_file}')
    print(f'Creating tar.gz file: {tar_gz_file}')
    with tarfile.open(tar_gz_file, 'w:gz') as tar:
        for file in files_to_zip:
            print(f'Adding file: {file}')
            tar.add(file, arcname=f'bitbi-{version}/bin/{os.path.basename(file)}')
    
'''
 # This file can create a *-release branch from current branch, and copy the sources to ../bitbi
 for building. It also replaces the keywords in the source files and creates a tar.gz file 
 with the binaries.
 
 # How to use?

source private-tools/.envbtc/bin/activate
python3 private-tools/release-bitb2.py

# Note:

Ater running the script, you can build the project in the ../bitbi directory.

 '''


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["clean", "build"], default="build")
    args = parser.parse_args()

    if args.mode == "clean":
        os.chdir(SRC_BTC)
        try:
            subprocess.run(['make maintainer-clean'], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f'ignore Error: {e}')
        
        delete_files_with_bitbi_in_name()
        git_reset_hard()
    else:
        # tar_gz_file('26.101.0')
        os.chdir(SRC_BTC)
        try:
            subprocess.run(['make maintainer-clean'], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f'ignore Error: {e}')
        
        delete_files_with_bitbi_in_name()
        git_reset_hard()
        try:
            version = create_release_branch()
            replace_keywords()
            subprocess.run([f"rsync -avzP --exclude='.git' --exclude='release-notes' --exclude={{'.gitignore','README.md','Makefile.in','desc/','desc.zip','.vscode','ci/','private-tools/','*.pc','*~','x86_64-pc-linux-gnu/','aclocal.m4'}} {SRC_BTC}/ {DEST_BITBI}/"], shell=True, check=True)
            
            # Build the project
            os.chdir(DEST_BITBI)
            subprocess.run(['./autogen.sh'], shell=True, check=True)
            subprocess.run(['./configure  --without-gui --disable-tests CPPFLAGS=" -I/home/buji/code/bitbi/pow/src" LIBS="-L/home/buji/code/bitbi/pow/build -lrandomx" CXXFLAGS="-O2"'], shell=True, check=True)
            subprocess.run(['make -j$(nproc)'], shell=True, check=True)
            tar_gz_file(version)
        except subprocess.CalledProcessError as e:
            print(f'Error: {e}')
            exit(1) 
        
        # back to origin branch for current workspace, and make it clean
        os.chdir(SRC_BTC)
        # try to check out to branch version
        try:
            subprocess.run([f"git checkout {version}"], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f'ignore Error: {e}')
        try:
            subprocess.run(['make maintainer-clean'], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f'ignore Error: {e}')
        
        delete_files_with_bitbi_in_name()
        git_reset_hard()