# max_supply = 0
# max_supply = 0
# max_supply = 0
# max_supply = 0
# #50=>35,000,000
# #50=>35,000,000
# #50=>35,000,000
# #50=>35,000,000
# #100=>70,000,000
# #100=>70,000,000
# #100=>70,000,000
# #100=>70,000,000
# #250=>175,000,000
# #250=>175,000,000
# #250=>175,000,000
# #250=>175,000,000
# block_reward = 99.99
# block_reward = 99.99
# block_reward = 99.99
# block_reward = 99.99
# block_time = 505  # minutes
# block_time = 505  # minutes
# block_time = 505  # minutes
# block_time = 505  # minutes
# seconds_per_year = 60 * 60 * 24 * 365
# seconds_per_year = 60 * 60 * 24 * 365
# seconds_per_year = 60 * 60 * 24 * 365
# seconds_per_year = 60 * 60 * 24 * 365
# blocks_per_halving = 250025#seconds_per_year * 2 / block_time
# blocks_per_halving = 250025#seconds_per_year * 2 / block_time
# blocks_per_halving = 250025#seconds_per_year * 2 / block_time
# blocks_per_halving = 250025#seconds_per_year * 2 / block_time
# print("blocks_per_halving:", blocks_per_halving)
# print("blocks_per_halving:", blocks_per_halving)
# print("blocks_per_halving:", blocks_per_halving)
# print("blocks_per_halving:", blocks_per_halving)
# years_per_halving = blocks_per_halving * block_time / seconds_per_year
# years_per_halving = blocks_per_halving * block_time / seconds_per_year
# years_per_halving = blocks_per_halving * block_time / seconds_per_year
# years_per_halving = blocks_per_halving * block_time / seconds_per_year
# print("years_per_halving:", years_per_halving)
# print("years_per_halving:", years_per_halving)
# print("years_per_halving:", years_per_halving)
# print("years_per_halving:", years_per_halving)
# # preferred_block_time = seconds_per_year*4/blocks_per_halving
# # preferred_block_time = seconds_per_year*4/blocks_per_halving
# # preferred_block_time = seconds_per_year*4/blocks_per_halving
# # preferred_block_time = seconds_per_year*4/blocks_per_halving
# # print("preferred_block_time:", preferred_block_time)
# # print("preferred_block_time:", preferred_block_time)
# # print("preferred_block_time:", preferred_block_time)
# # print("preferred_block_time:", preferred_block_time)
# while block_reward/4 > 0:
# while block_reward/4 > 0:
# while block_reward/4 > 0:
# while block_reward/4 > 0:
#     # Add the total reward for this halving period
#     # Add the total reward for this halving period
#     # Add the total reward for this halving period
#     # Add the total reward for this halving period
#     max_supply += block_reward * blocks_per_halving
#     max_supply += block_reward * blocks_per_halving
#     max_supply += block_reward * blocks_per_halving
#     max_supply += block_reward * blocks_per_halving
#     # Reduce the block reward by a quarter for the next period
#     # Reduce the block reward by a quarter for the next period
#     # Reduce the block reward by a quarter for the next period
#     # Reduce the block reward by a quarter for the next period
#     block_reward -= block_reward/ 4
#     block_reward -= block_reward/ 4
#     block_reward -= block_reward/ 4
#     block_reward -= block_reward/ 4




# # Convert to smallest unit
# # Convert to smallest unit
# # Convert to smallest unit
# # Convert to smallest unit
# max_supply *= 1e8
# max_supply *= 1e8
# max_supply *= 1e8
# max_supply *= 1e8
# # 63714326
# # 63714326
# # 63714326
# # 63714326
# print(f"The maximum supply of the coin is {max_supply} smallest units or {max_supply / 1e8} coins.")
# print(f"The maximum supply of the coin is {max_supply} smallest units or {max_supply / 1e8} coins.")
# print(f"The maximum supply of the coin is {max_supply} smallest units or {max_supply / 1e8} coins.")
# print(f"The maximum supply of the coin is {max_supply} smallest units or {max_supply / 1e8} coins.")








def cal_total_supply(block_reward, blocks_per_halving):
def cal_total_supply(block_reward, blocks_per_halving):
def cal_total_supply(block_reward, blocks_per_halving):
def cal_total_supply(block_reward, blocks_per_halving):
    max_supply=0
    max_supply=0
    max_supply=0
    max_supply=0
    drop = block_reward // 4
    drop = block_reward // 4
    drop = block_reward // 4
    drop = block_reward // 4
    while block_reward - drop >= 101:
    while block_reward - drop >= 101:
    while block_reward - drop >= 101:
    while block_reward - drop >= 101:
        # Add the total reward for this halving period
        # Add the total reward for this halving period
        # Add the total reward for this halving period
        # Add the total reward for this halving period
        max_supply += block_reward * blocks_per_halving
        max_supply += block_reward * blocks_per_halving
        max_supply += block_reward * blocks_per_halving
        max_supply += block_reward * blocks_per_halving
        # Reduce the block reward by a quarter for the next period
        # Reduce the block reward by a quarter for the next period
        # Reduce the block reward by a quarter for the next period
        # Reduce the block reward by a quarter for the next period
        block_reward -= drop
        block_reward -= drop
        block_reward -= drop
        block_reward -= drop
    return max_supply
    return max_supply
    return max_supply
    return max_supply




COIN = 1e8
COIN = 1e8
COIN = 1e8
COIN = 1e8




def main():
def main():
def main():
def main():
    bn = 50*COIN
    bn = 50*COIN
    bn = 50*COIN
    bn = 50*COIN
    reward = bn*101//100
    reward = bn*101//100
    reward = bn*101//100
    reward = bn*101//100
  
  
  
  
    while reward < 556*COIN:
    while reward < 556*COIN:
    while reward < 556*COIN:
    while reward < 556*COIN:
        blocks_per_halving= 60000 - 100
        blocks_per_halving= 60000 - 100
        blocks_per_halving= 60000 - 100
        blocks_per_halving= 60000 - 100
        while blocks_per_halving < 400000:
        while blocks_per_halving < 400000:
        while blocks_per_halving < 400000:
        while blocks_per_halving < 400000:
            premine = 5*1e5*COIN
            premine = 5*1e5*COIN
            premine = 5*1e5*COIN
            premine = 5*1e5*COIN
            while premine < 1e6*COIN:
            while premine < 1e6*COIN:
            while premine < 1e6*COIN:
            while premine < 1e6*COIN:
                max_supply = cal_total_supply(reward, blocks_per_halving) + premine
                max_supply = cal_total_supply(reward, blocks_per_halving) + premine
                max_supply = cal_total_supply(reward, blocks_per_halving) + premine
                max_supply = cal_total_supply(reward, blocks_per_halving) + premine
                if max_supply + 1e6*COIN < 5 *1e7*COIN:
                if max_supply + 1e6*COIN < 5 *1e7*COIN:
                if max_supply + 1e6*COIN < 5 *1e7*COIN:
                if max_supply + 1e6*COIN < 5 *1e7*COIN:
                    break
                    break
                    break
                    break
                if max_supply < 5*1e7*COIN:
                if max_supply < 5*1e7*COIN:
                if max_supply < 5*1e7*COIN:
                if max_supply < 5*1e7*COIN:
                    continue
                    continue
                    continue
                    continue
                if (max_supply - max_supply // (1e7*COIN) * (1e7*COIN)) < 100*COIN:
                if (max_supply - max_supply // (1e7*COIN) * (1e7*COIN)) < 100*COIN:
                if (max_supply - max_supply // (1e7*COIN) * (1e7*COIN)) < 100*COIN:
                if (max_supply - max_supply // (1e7*COIN) * (1e7*COIN)) < 100*COIN:
                    print(f"good max_supply found: {max_supply // COIN} reward: {reward // COIN} \
                    print(f"good max_supply found: {max_supply // COIN} reward: {reward // COIN} \
                    print(f"good max_supply found: {max_supply // COIN} reward: {reward // COIN} \
                    print(f"good max_supply found: {max_supply // COIN} reward: {reward // COIN} \
                        blocks_per_halving: {blocks_per_halving}")
                        blocks_per_halving: {blocks_per_halving}")
                        blocks_per_halving: {blocks_per_halving}")
                        blocks_per_halving: {blocks_per_halving}")
                
                
                
                
                int10000 = round(blocks_per_halving / 10000) * 10000
                int10000 = round(blocks_per_halving / 10000) * 10000
                int10000 = round(blocks_per_halving / 10000) * 10000
                int10000 = round(blocks_per_halving / 10000) * 10000
                if abs(int10000 - blocks_per_halving) > 100:
                if abs(int10000 - blocks_per_halving) > 100:
                if abs(int10000 - blocks_per_halving) > 100:
                if abs(int10000 - blocks_per_halving) > 100:
                    blocks_per_halving = int10000 + 10000
                    blocks_per_halving = int10000 + 10000
                    blocks_per_halving = int10000 + 10000
                    blocks_per_halving = int10000 + 10000




                premine += 100*COIN
                premine += 100*COIN
                premine += 100*COIN
                premine += 100*COIN
            
            
            
            
            blocks_per_halving += 1
            blocks_per_halving += 1
            blocks_per_halving += 1
            blocks_per_halving += 1
        bn+=1*COIN
        bn+=1*COIN
        bn+=1*COIN
        bn+=1*COIN
        reward = bn*101//100
        reward = bn*101//100
        reward = bn*101//100
        reward = bn*101//100




main()
main()
main()
main()




# good max_supply found: 99999795.99999999 (has 1million premine) reward: 98.98                       blocks_per_halving: 250050
# good max_supply found: 99999795.99999999 (has 1million premine) reward: 98.98                       blocks_per_halving: 250050
# good max_supply found: 99999795.99999999 (has 1million premine) reward: 98.98                       blocks_per_halving: 250050
# good max_supply found: 99999795.99999999 (has 1million premine) reward: 98.98                       blocks_per_halving: 250050
# reward 25
# reward 25
# reward 25
# reward 25
# block_time:253s blocks_per_halving: 250000 max_supply: 25,000,000           
# block_time:253s blocks_per_halving: 250000 max_supply: 25,000,000           
# block_time:253s blocks_per_halving: 250000 max_supply: 25,000,000           
# block_time:253s blocks_per_halving: 250000 max_supply: 25,000,000           
# block_time:150s blocks_per_halving: 420000 max_supply: 42,000,000
# block_time:150s blocks_per_halving: 420000 max_supply: 42,000,000
# block_time:150s blocks_per_halving: 420000 max_supply: 42,000,000
# block_time:150s blocks_per_halving: 420000 max_supply: 42,000,000
# block_time:100s blocks_per_halving: 630000 max_supply: 63,000,000
# block_time:100s blocks_per_halving: 630000 max_supply: 63,000,000
# block_time:100s blocks_per_halving: 630000 max_supply: 63,000,000
# block_time:100s blocks_per_halving: 630000 max_supply: 63,000,000
# reward 250                                                                                                             
# reward 250                                                                                                             
# reward 250                                                                                                             
# reward 250                                                                                                             
# block_time:630s blocks_per_halving: 100000 max_supply: 100,000,000
# block_time:630s blocks_per_halving: 100000 max_supply: 100,000,000
# block_time:630s blocks_per_halving: 100000 max_supply: 100,000,000
# block_time:630s blocks_per_halving: 100000 max_supply: 100,000,000
# block_time:420s blocks_per_halving: 150000 max_supply: 150,000,000
# block_time:420s blocks_per_halving: 150000 max_supply: 150,000,000
# block_time:420s blocks_per_halving: 150000 max_supply: 150,000,000
# block_time:420s blocks_per_halving: 150000 max_supply: 150,000,000
# block_time:315s blocks_per_halving: 200000 max_supply: 200,000,000
# block_time:315s blocks_per_halving: 200000 max_supply: 200,000,000
# block_time:315s blocks_per_halving: 200000 max_supply: 200,000,000
# block_time:315s blocks_per_halving: 200000 max_supply: 200,000,000
# block_time:210s blocks_per_halving: 300000 max_supply: 300,000,000
# block_time:210s blocks_per_halving: 300000 max_supply: 300,000,000
# block_time:210s blocks_per_halving: 300000 max_supply: 300,000,000
# block_time:210s blocks_per_halving: 300000 max_supply: 300,000,000
# block_time:105s blocks_per_halving: 600000 max_supply: 600,000,000
# block_time:105s blocks_per_halving: 600000 max_supply: 600,000,000
# block_time:105s blocks_per_halving: 600000 max_supply: 600,000,000
# block_time:105s blocks_per_halving: 600000 max_supply: 600,000,000
# good max_supply found: 50000000.0 reward: 25                       blocks_per_halving: 500000
# good max_supply found: 50000000.0 reward: 25                       blocks_per_halving: 500000
# good max_supply found: 50000000.0 reward: 25                       blocks_per_halving: 500000
# good max_supply found: 50000000.0 reward: 25                       blocks_per_halving: 500000
# good max_supply found: 50000000.0 reward: 40                       blocks_per_halving: 312500
# good max_supply found: 50000000.0 reward: 40                       blocks_per_halving: 312500
# good max_supply found: 50000000.0 reward: 40                       blocks_per_halving: 312500
# good max_supply found: 50000000.0 reward: 40                       blocks_per_halving: 312500
# good max_supply found: 50000000.0 reward: 50                       blocks_per_halving: 250000
# good max_supply found: 50000000.0 reward: 50                       blocks_per_halving: 250000
# good max_supply found: 50000000.0 reward: 50                       blocks_per_halving: 250000
# good max_supply found: 50000000.0 reward: 50                       blocks_per_halving: 250000
# good max_supply found: 100000000.0 reward: 50                       blocks_per_halving: 500000
# good max_supply found: 100000000.0 reward: 50                       blocks_per_halving: 500000
# good max_supply found: 100000000.0 reward: 50                       blocks_per_halving: 500000
# good max_supply found: 100000000.0 reward: 50                       blocks_per_halving: 500000
# good max_supply found: 50000000.0 reward: 80                       blocks_per_halving: 156250
# good max_supply found: 50000000.0 reward: 80                       blocks_per_halving: 156250
# good max_supply found: 50000000.0 reward: 80                       blocks_per_halving: 156250
# good max_supply found: 50000000.0 reward: 80                       blocks_per_halving: 156250
# good max_supply found: 100000000.0 reward: 80                       blocks_per_halving: 312500
# good max_supply found: 100000000.0 reward: 80                       blocks_per_halving: 312500
# good max_supply found: 100000000.0 reward: 80                       blocks_per_halving: 312500
# good max_supply found: 100000000.0 reward: 80                       blocks_per_halving: 312500
# good max_supply found: 50000000.0 reward: 100                       blocks_per_halving: 125000
# good max_supply found: 50000000.0 reward: 100                       blocks_per_halving: 125000
# good max_supply found: 50000000.0 reward: 100                       blocks_per_halving: 125000
# good max_supply found: 50000000.0 reward: 100                       blocks_per_halving: 125000
# good max_supply found: 100000000.0 reward: 100                       blocks_per_halving: 250000
# good max_supply found: 100000000.0 reward: 100                       blocks_per_halving: 250000
# good max_supply found: 100000000.0 reward: 100                       blocks_per_halving: 250000
# good max_supply found: 100000000.0 reward: 100                       blocks_per_halving: 250000
# good max_supply found: 200000000.0 reward: 100                       blocks_per_halving: 500000
# good max_supply found: 200000000.0 reward: 100                       blocks_per_halving: 500000
# good max_supply found: 200000000.0 reward: 100                       blocks_per_halving: 500000
# good max_supply found: 200000000.0 reward: 100                       blocks_per_halving: 500000
# good max_supply found: 50000000.0 reward: 125                       blocks_per_halving: 100000
# good max_supply found: 50000000.0 reward: 125                       blocks_per_halving: 100000
# good max_supply found: 50000000.0 reward: 125                       blocks_per_halving: 100000
# good max_supply found: 50000000.0 reward: 125                       blocks_per_halving: 100000
# good max_supply found: 100000000.0 reward: 125                       blocks_per_halving: 200000
# good max_supply found: 100000000.0 reward: 125                       blocks_per_halving: 200000
# good max_supply found: 100000000.0 reward: 125                       blocks_per_halving: 200000
# good max_supply found: 100000000.0 reward: 125                       blocks_per_halving: 200000
# good max_supply found: 200000000.0 reward: 125                       blocks_per_halving: 400000
# good max_supply found: 200000000.0 reward: 125                       blocks_per_halving: 400000
# good max_supply found: 200000000.0 reward: 125                       blocks_per_halving: 400000
# good max_supply found: 200000000.0 reward: 125                       blocks_per_halving: 400000
# good max_supply found: 300000000.0 reward: 150                       blocks_per_halving: 500000
# good max_supply found: 300000000.0 reward: 150                       blocks_per_halving: 500000
# good max_supply found: 300000000.0 reward: 150                       blocks_per_halving: 500000
# good max_supply found: 300000000.0 reward: 150                       blocks_per_halving: 500000
# good max_supply found: 100000000.0 reward: 160                       blocks_per_halving: 156250
# good max_supply found: 100000000.0 reward: 160                       blocks_per_halving: 156250
# good max_supply found: 100000000.0 reward: 160                       blocks_per_halving: 156250
# good max_supply found: 100000000.0 reward: 160                       blocks_per_halving: 156250
# good max_supply found: 200000000.0 reward: 160                       blocks_per_halving: 312500
# good max_supply found: 200000000.0 reward: 160                       blocks_per_halving: 312500
# good max_supply found: 200000000.0 reward: 160                       blocks_per_halving: 312500
# good max_supply found: 200000000.0 reward: 160                       blocks_per_halving: 312500
# good max_supply found: 300000000.0 reward: 160                       blocks_per_halving: 468750
# good max_supply found: 300000000.0 reward: 160                       blocks_per_halving: 468750
# good max_supply found: 300000000.0 reward: 160                       blocks_per_halving: 468750
# good max_supply found: 300000000.0 reward: 160                       blocks_per_halving: 468750
# good max_supply found: 50000000.0 reward: 200                       blocks_per_halving: 62500
# good max_supply found: 50000000.0 reward: 200                       blocks_per_halving: 62500
# good max_supply found: 50000000.0 reward: 200                       blocks_per_halving: 62500
# good max_supply found: 50000000.0 reward: 200                       blocks_per_halving: 62500
# good max_supply found: 100000000.0 reward: 200                       blocks_per_halving: 125000
# good max_supply found: 100000000.0 reward: 200                       blocks_per_halving: 125000
# good max_supply found: 100000000.0 reward: 200                       blocks_per_halving: 125000
# good max_supply found: 100000000.0 reward: 200                       blocks_per_halving: 125000
# good max_supply found: 200000000.0 reward: 200                       blocks_per_halving: 250000
# good max_supply found: 200000000.0 reward: 200                       blocks_per_halving: 250000
# good max_supply found: 200000000.0 reward: 200                       blocks_per_halving: 250000
# good max_supply found: 200000000.0 reward: 200                       blocks_per_halving: 250000
# good max_supply found: 300000000.0 reward: 200                       blocks_per_halving: 375000
# good max_supply found: 300000000.0 reward: 200                       blocks_per_halving: 375000
# good max_supply found: 300000000.0 reward: 200                       blocks_per_halving: 375000
# good max_supply found: 300000000.0 reward: 200                       blocks_per_halving: 375000
# good max_supply found: 400000000.0 reward: 200                       blocks_per_halving: 500000
# good max_supply found: 400000000.0 reward: 200                       blocks_per_halving: 500000
# good max_supply found: 400000000.0 reward: 200                       blocks_per_halving: 500000
# good max_supply found: 400000000.0 reward: 200                       blocks_per_halving: 500000
# good max_supply found: 300000000.0 reward: 240                       blocks_per_halving: 312500
# good max_supply found: 300000000.0 reward: 240                       blocks_per_halving: 312500
# good max_supply found: 300000000.0 reward: 240                       blocks_per_halving: 312500
# good max_supply found: 300000000.0 reward: 240                       blocks_per_halving: 312500
# good max_supply found: 50000000.0 reward: 250                       blocks_per_halving: 50000
# good max_supply found: 50000000.0 reward: 250                       blocks_per_halving: 50000
# good max_supply found: 50000000.0 reward: 250                       blocks_per_halving: 50000
# good max_supply found: 50000000.0 reward: 250                       blocks_per_halving: 50000
# good max_supply found: 100000000.0 reward: 250                       blocks_per_halving: 100000
# good max_supply found: 100000000.0 reward: 250                       blocks_per_halving: 100000
# good max_supply found: 100000000.0 reward: 250                       blocks_per_halving: 100000
# good max_supply found: 100000000.0 reward: 250                       blocks_per_halving: 100000
# good max_supply found: 200000000.0 reward: 250                       blocks_per_halving: 200000
# good max_supply found: 200000000.0 reward: 250                       blocks_per_halving: 200000
# good max_supply found: 200000000.0 reward: 250                       blocks_per_halving: 200000
# good max_supply found: 200000000.0 reward: 250                       blocks_per_halving: 200000
# good max_supply found: 300000000.0 reward: 250                       blocks_per_halving: 300000
# good max_supply found: 300000000.0 reward: 250                       blocks_per_halving: 300000
# good max_supply found: 300000000.0 reward: 250                       blocks_per_halving: 300000
# good max_supply found: 300000000.0 reward: 250                       blocks_per_halving: 300000
# good max_supply found: 400000000.0 reward: 250                       blocks_per_halving: 400000
# good max_supply found: 400000000.0 reward: 250                       blocks_per_halving: 400000
# good max_supply found: 400000000.0 reward: 250                       blocks_per_halving: 400000
# good max_supply found: 400000000.0 reward: 250                       blocks_per_halving: 400000
# good max_supply found: 300000000.0 reward: 300                       blocks_per_halving: 250000
# good max_supply found: 300000000.0 reward: 300                       blocks_per_halving: 250000
# good max_supply found: 300000000.0 reward: 300                       blocks_per_halving: 250000
# good max_supply found: 300000000.0 reward: 300                       blocks_per_halving: 250000
# good max_supply found: 600000000.0 reward: 300                       blocks_per_halving: 500000
# good max_supply found: 600000000.0 reward: 300                       blocks_per_halving: 500000
# good max_supply found: 600000000.0 reward: 300                       blocks_per_halving: 500000
# good max_supply found: 600000000.0 reward: 300                       blocks_per_halving: 500000
# good max_supply found: 200000000.0 reward: 320                       blocks_per_halving: 156250
# good max_supply found: 200000000.0 reward: 320                       blocks_per_halving: 156250
# good max_supply found: 200000000.0 reward: 320                       blocks_per_halving: 156250
# good max_supply found: 200000000.0 reward: 320                       blocks_per_halving: 156250
# good max_supply found: 400000000.0 reward: 320                       blocks_per_halving: 312500
# good max_supply found: 400000000.0 reward: 320                       blocks_per_halving: 312500
# good max_supply found: 400000000.0 reward: 320                       blocks_per_halving: 312500
# good max_supply found: 400000000.0 reward: 320                       blocks_per_halving: 312500
# good max_supply found: 600000000.0 reward: 320                       blocks_per_halving: 468750
# good max_supply found: 600000000.0 reward: 320                       blocks_per_halving: 468750
# good max_supply found: 600000000.0 reward: 320                       blocks_per_halving: 468750
# good max_supply found: 600000000.0 reward: 320                       blocks_per_halving: 468750
# good max_supply found: 300000000.0 reward: 375                       blocks_per_halving: 200000
# good max_supply found: 300000000.0 reward: 375                       blocks_per_halving: 200000
# good max_supply found: 300000000.0 reward: 375                       blocks_per_halving: 200000
# good max_supply found: 300000000.0 reward: 375                       blocks_per_halving: 200000
# good max_supply found: 600000000.0 reward: 375                       blocks_per_halving: 400000
# good max_supply found: 600000000.0 reward: 375                       blocks_per_halving: 400000
# good max_supply found: 600000000.0 reward: 375                       blocks_per_halving: 400000
# good max_supply found: 600000000.0 reward: 375                       blocks_per_halving: 400000
# good max_supply found: 50000000.0 reward: 400                       blocks_per_halving: 31250
# good max_supply found: 50000000.0 reward: 400                       blocks_per_halving: 31250
# good max_supply found: 50000000.0 reward: 400                       blocks_per_halving: 31250
# good max_supply found: 50000000.0 reward: 400                       blocks_per_halving: 31250
# good max_supply found: 100000000.0 reward: 400                       blocks_per_halving: 62500
# good max_supply found: 100000000.0 reward: 400                       blocks_per_halving: 62500
# good max_supply found: 100000000.0 reward: 400                       blocks_per_halving: 62500
# good max_supply found: 100000000.0 reward: 400                       blocks_per_halving: 62500
# good max_supply found: 200000000.0 reward: 400                       blocks_per_halving: 125000
# good max_supply found: 200000000.0 reward: 400                       blocks_per_halving: 125000
# good max_supply found: 200000000.0 reward: 400                       blocks_per_halving: 125000
# good max_supply found: 200000000.0 reward: 400                       blocks_per_halving: 125000
# good max_supply found: 300000000.0 reward: 400                       blocks_per_halving: 187500
# good max_supply found: 300000000.0 reward: 400                       blocks_per_halving: 187500
# good max_supply found: 300000000.0 reward: 400                       blocks_per_halving: 187500
# good max_supply found: 300000000.0 reward: 400                       blocks_per_halving: 187500
# good max_supply found: 400000000.0 reward: 400                       blocks_per_halving: 250000
# good max_supply found: 400000000.0 reward: 400                       blocks_per_halving: 250000
# good max_supply found: 400000000.0 reward: 400                       blocks_per_halving: 250000
# good max_supply found: 400000000.0 reward: 400                       blocks_per_halving: 250000
# good max_supply found: 600000000.0 reward: 400                       blocks_per_halving: 375000
# good max_supply found: 600000000.0 reward: 400                       blocks_per_halving: 375000
# good max_supply found: 600000000.0 reward: 400                       blocks_per_halving: 375000
# good max_supply found: 600000000.0 reward: 400                       blocks_per_halving: 375000
# good max_supply found: 800000000.0 reward: 400                       blocks_per_halving: 500000
# good max_supply found: 800000000.0 reward: 400                       blocks_per_halving: 500000
# good max_supply found: 800000000.0 reward: 400                       blocks_per_halving: 500000
# good max_supply found: 800000000.0 reward: 400                       blocks_per_halving: 500000
# good max_supply found: 300000000.0 reward: 480                       blocks_per_halving: 156250
# good max_supply found: 300000000.0 reward: 480                       blocks_per_halving: 156250
# good max_supply found: 300000000.0 reward: 480                       blocks_per_halving: 156250
# good max_supply found: 300000000.0 reward: 480                       blocks_per_halving: 156250
# good max_supply found: 600000000.0 reward: 480                       blocks_per_halving: 312500
# good max_supply found: 600000000.0 reward: 480                       blocks_per_halving: 312500
# good max_supply found: 600000000.0 reward: 480                       blocks_per_halving: 312500
# good max_supply found: 600000000.0 reward: 480                       blocks_per_halving: 312500
# good max_supply found: 1020000000.0 reward: 480                       blocks_per_halving: 531250
# good max_supply found: 1020000000.0 reward: 480                       blocks_per_halving: 531250
# good max_supply found: 1020000000.0 reward: 480                       blocks_per_halving: 531250
# good max_supply found: 1020000000.0 reward: 480                       blocks_per_halving: 531250
# good max_supply found: 50000000.0 reward: 500                       blocks_per_halving: 25000
# good max_supply found: 50000000.0 reward: 500                       blocks_per_halving: 25000
# good max_supply found: 50000000.0 reward: 500                       blocks_per_halving: 25000
# good max_supply found: 50000000.0 reward: 500                       blocks_per_halving: 25000
# good max_supply found: 100000000.0 reward: 500                       blocks_per_halving: 50000
# good max_supply found: 100000000.0 reward: 500                       blocks_per_halving: 50000
# good max_supply found: 100000000.0 reward: 500                       blocks_per_halving: 50000
# good max_supply found: 100000000.0 reward: 500                       blocks_per_halving: 50000
# good max_supply found: 200000000.0 reward: 500                       blocks_per_halving: 100000
# good max_supply found: 200000000.0 reward: 500                       blocks_per_halving: 100000
# good max_supply found: 200000000.0 reward: 500                       blocks_per_halving: 100000
# good max_supply found: 200000000.0 reward: 500                       blocks_per_halving: 100000
# good max_supply found: 300000000.0 reward: 500                       blocks_per_halving: 150000
# good max_supply found: 300000000.0 reward: 500                       blocks_per_halving: 150000
# good max_supply found: 300000000.0 reward: 500                       blocks_per_halving: 150000
# good max_supply found: 300000000.0 reward: 500                       blocks_per_halving: 150000
# good max_supply found: 400000000.0 reward: 500                       blocks_per_halving: 200000
# good max_supply found: 400000000.0 reward: 500                       blocks_per_halving: 200000
# good max_supply found: 400000000.0 reward: 500                       blocks_per_halving: 200000
# good max_supply found: 400000000.0 reward: 500                       blocks_per_halving: 200000
# good max_supply found: 600000000.0 reward: 500                       blocks_per_halving: 300000
# good max_supply found: 600000000.0 reward: 500                       blocks_per_halving: 300000
# good max_supply found: 600000000.0 reward: 500                       blocks_per_halving: 300000
# good max_supply found: 600000000.0 reward: 500                       blocks_per_halving: 300000
# good max_supply found: 800000000.0 reward: 500                       blocks_per_halving: 400000
# good max_supply found: 800000000.0 reward: 500                       blocks_per_halving: 400000
# good max_supply found: 800000000.0 reward: 500                       blocks_per_halving: 400000
# good max_supply found: 800000000.0 reward: 500                       blocks_per_halving: 400000
# good max_supply found: 1020000000.0 reward: 500                       blocks_per_halving: 510000
# good max_supply found: 1020000000.0 reward: 500                       blocks_per_halving: 510000
# good max_supply found: 1020000000.0 reward: 500                       blocks_per_halving: 510000
# good max_supply found: 1020000000.0 reward: 500                       blocks_per_halving: 510000
# good max_supply found: 1020000000.0 reward: 510                       blocks_per_halving: 500000
# good max_supply found: 1020000000.0 reward: 510                       blocks_per_halving: 500000
# good max_supply found: 1020000000.0 reward: 510                       blocks_per_halving: 500000
# good max_supply found: 1020000000.0 reward: 510                       blocks_per_halving: 500000
# good max_supply found: 1020000000.0 reward: 544                       blocks_per_halving: 468750
# good max_supply found: 1020000000.0 reward: 544                       blocks_per_halving: 468750
# good max_supply found: 1020000000.0 reward: 544                       blocks_per_halving: 468750
# good max_supply found: 1020000000.0 reward: 544                       blocks_per_halving: 468750
# good max_supply found: 300000000.0 reward: 600                       blocks_per_halving: 125000
# good max_supply found: 300000000.0 reward: 600                       blocks_per_halving: 125000
# good max_supply found: 300000000.0 reward: 600                       blocks_per_halving: 125000
# good max_supply found: 300000000.0 reward: 600                       blocks_per_halving: 125000
# good max_supply found: 600000000.0 reward: 600                       blocks_per_halving: 250000
# good max_supply found: 600000000.0 reward: 600                       blocks_per_halving: 250000
# good max_supply found: 600000000.0 reward: 600                       blocks_per_halving: 250000
# good max_supply found: 600000000.0 reward: 600                       blocks_per_halving: 250000
# good max_supply found: 1020000000.0 reward: 600                       blocks_per_halving: 425000
# good max_supply found: 1020000000.0 reward: 600                       blocks_per_halving: 425000
# good max_supply found: 1020000000.0 reward: 600                       blocks_per_halving: 425000
# good max_supply found: 1020000000.0 reward: 600                       blocks_per_halving: 425000
# good max_supply found: 50000000.0 reward: 625                       blocks_per_halving: 20000
# good max_supply found: 50000000.0 reward: 625                       blocks_per_halving: 20000
# good max_supply found: 50000000.0 reward: 625                       blocks_per_halving: 20000
# good max_supply found: 50000000.0 reward: 625                       blocks_per_halving: 20000
# good max_supply found: 100000000.0 reward: 625                       blocks_per_halving: 40000
# good max_supply found: 100000000.0 reward: 625                       blocks_per_halving: 40000
# good max_supply found: 100000000.0 reward: 625                       blocks_per_halving: 40000
# good max_supply found: 100000000.0 reward: 625                       blocks_per_halving: 40000
# good max_supply found: 200000000.0 reward: 625                       blocks_per_halving: 80000
# good max_supply found: 200000000.0 reward: 625                       blocks_per_halving: 80000
# good max_supply found: 200000000.0 reward: 625                       blocks_per_halving: 80000
# good max_supply found: 200000000.0 reward: 625                       blocks_per_halving: 80000
# good max_supply found: 300000000.0 reward: 625                       blocks_per_halving: 120000
# good max_supply found: 300000000.0 reward: 625                       blocks_per_halving: 120000
# good max_supply found: 300000000.0 reward: 625                       blocks_per_halving: 120000
# good max_supply found: 300000000.0 reward: 625                       blocks_per_halving: 120000
# good max_supply found: 400000000.0 reward: 625                       blocks_per_halving: 160000
# good max_supply found: 400000000.0 reward: 625                       blocks_per_halving: 160000
# good max_supply found: 400000000.0 reward: 625                       blocks_per_halving: 160000
# good max_supply found: 400000000.0 reward: 625                       blocks_per_halving: 160000
# good max_supply found: 600000000.0 reward: 625                       blocks_per_halving: 240000
# good max_supply found: 600000000.0 reward: 625                       blocks_per_halving: 240000
# good max_supply found: 600000000.0 reward: 625                       blocks_per_halving: 240000
# good max_supply found: 600000000.0 reward: 625                       blocks_per_halving: 240000
# good max_supply found: 800000000.0 reward: 625                       blocks_per_halving: 320000
# good max_supply found: 800000000.0 reward: 625                       blocks_per_halving: 320000
# good max_supply found: 800000000.0 reward: 625                       blocks_per_halving: 320000
# good max_supply found: 800000000.0 reward: 625                       blocks_per_halving: 320000
# good max_supply found: 1020000000.0 reward: 625                       blocks_per_halving: 408000
# good max_supply found: 1020000000.0 reward: 625                       blocks_per_halving: 408000
# good max_supply found: 1020000000.0 reward: 625                       blocks_per_halving: 408000
# good max_supply found: 1020000000.0 reward: 625                       blocks_per_halving: 408000
# good max_supply found: 400000000.0 reward: 640                       blocks_per_halving: 156250
# good max_supply found: 400000000.0 reward: 640                       blocks_per_halving: 156250
# good max_supply found: 400000000.0 reward: 640                       blocks_per_halving: 156250
# good max_supply found: 400000000.0 reward: 640                       blocks_per_halving: 156250
# good max_supply found: 800000000.0 reward: 640                       blocks_per_halving: 312500
# good max_supply found: 800000000.0 reward: 640                       blocks_per_halving: 312500
# good max_supply found: 800000000.0 reward: 640                       blocks_per_halving: 312500
# good max_supply found: 800000000.0 reward: 640                       blocks_per_halving: 312500
# good max_supply found: 1020000000.0 reward: 680                       blocks_per_halving: 375000
# good max_supply found: 1020000000.0 reward: 680                       blocks_per_halving: 375000
# good max_supply found: 1020000000.0 reward: 680                       blocks_per_halving: 375000
# good max_supply found: 1020000000.0 reward: 680                       blocks_per_halving: 375000
# good max_supply found: 300000000.0 reward: 750                       blocks_per_halving: 100000
# good max_supply found: 300000000.0 reward: 750                       blocks_per_halving: 100000
# good max_supply found: 300000000.0 reward: 750                       blocks_per_halving: 100000
# good max_supply found: 300000000.0 reward: 750                       blocks_per_halving: 100000
# good max_supply found: 600000000.0 reward: 750                       blocks_per_halving: 200000
# good max_supply found: 600000000.0 reward: 750                       blocks_per_halving: 200000
# good max_supply found: 600000000.0 reward: 750                       blocks_per_halving: 200000
# good max_supply found: 600000000.0 reward: 750                       blocks_per_halving: 200000
# good max_supply found: 1020000000.0 reward: 750                       blocks_per_halving: 340000
# good max_supply found: 1020000000.0 reward: 750                       blocks_per_halving: 340000
# good max_supply found: 1020000000.0 reward: 750                       blocks_per_halving: 340000
# good max_supply found: 1020000000.0 reward: 750                       blocks_per_halving: 340000
# good max_supply found: 100000000.0 reward: 800                       blocks_per_halving: 31250
# good max_supply found: 100000000.0 reward: 800                       blocks_per_halving: 31250
# good max_supply found: 100000000.0 reward: 800                       blocks_per_halving: 31250
# good max_supply found: 100000000.0 reward: 800                       blocks_per_halving: 31250
# good max_supply found: 200000000.0 reward: 800                       blocks_per_halving: 62500
# good max_supply found: 200000000.0 reward: 800                       blocks_per_halving: 62500
# good max_supply found: 200000000.0 reward: 800                       blocks_per_halving: 62500
# good max_supply found: 200000000.0 reward: 800                       blocks_per_halving: 62500
# good max_supply found: 300000000.0 reward: 800                       blocks_per_halving: 93750
# good max_supply found: 300000000.0 reward: 800                       blocks_per_halving: 93750
# good max_supply found: 300000000.0 reward: 800                       blocks_per_halving: 93750
# good max_supply found: 300000000.0 reward: 800                       blocks_per_halving: 93750
# good max_supply found: 400000000.0 reward: 800                       blocks_per_halving: 125000
# good max_supply found: 400000000.0 reward: 800                       blocks_per_halving: 125000
# good max_supply found: 400000000.0 reward: 800                       blocks_per_halving: 125000
# good max_supply found: 400000000.0 reward: 800                       blocks_per_halving: 125000
# good max_supply found: 600000000.0 reward: 800                       blocks_per_halving: 187500
# good max_supply found: 600000000.0 reward: 800                       blocks_per_halving: 187500
# good max_supply found: 600000000.0 reward: 800                       blocks_per_halving: 187500
# good max_supply found: 600000000.0 reward: 800                       blocks_per_halving: 187500
# good max_supply found: 800000000.0 reward: 800                       blocks_per_halving: 250000
# good max_supply found: 800000000.0 reward: 800                       blocks_per_halving: 250000
# good max_supply found: 800000000.0 reward: 800                       blocks_per_halving: 250000
# good max_supply found: 800000000.0 reward: 800                       blocks_per_halving: 250000
# good max_supply found: 1020000000.0 reward: 800                       blocks_per_halving: 318750
# good max_supply found: 1020000000.0 reward: 800                       blocks_per_halving: 318750
# good max_supply found: 1020000000.0 reward: 800                       blocks_per_halving: 318750
# good max_supply found: 1020000000.0 reward: 800                       blocks_per_halving: 318750
# good max_supply found: 1020000000.0 reward: 816                       blocks_per_halving: 312500
# good max_supply found: 1020000000.0 reward: 816                       blocks_per_halving: 312500
# good max_supply found: 1020000000.0 reward: 816                       blocks_per_halving: 312500
# good max_supply found: 1020000000.0 reward: 816                       blocks_per_halving: 312500
# good max_supply found: 1020000000.0 reward: 850                       blocks_per_halving: 300000
# good max_supply found: 1020000000.0 reward: 850                       blocks_per_halving: 300000
# good max_supply found: 1020000000.0 reward: 850                       blocks_per_halving: 300000
# good max_supply found: 1020000000.0 reward: 850                       blocks_per_halving: 300000
# good max_supply found: 600000000.0 reward: 960                       blocks_per_halving: 156250
# good max_supply found: 600000000.0 reward: 960                       blocks_per_halving: 156250
# good max_supply found: 600000000.0 reward: 960                       blocks_per_halving: 156250
# good max_supply found: 600000000.0 reward: 960                       blocks_per_halving: 156250








# good max_supply found: 109999382.79999997 reward: 47.46999999999999                       blocks_per_halving: 579310
# good max_supply found: 109999382.79999997 reward: 47.46999999999999                       blocks_per_halving: 579310
# good max_supply found: 109999382.79999997 reward: 47.46999999999999                       blocks_per_halving: 579310
# good max_supply found: 109999382.79999997 reward: 47.46999999999999                       blocks_per_halving: 579310
# good max_supply found: 109999180.79999995 reward: 48.47999999999999                       blocks_per_halving: 567240
# good max_supply found: 109999180.79999995 reward: 48.47999999999999                       blocks_per_halving: 567240
# good max_supply found: 109999180.79999995 reward: 48.47999999999999                       blocks_per_halving: 567240
# good max_supply found: 109999180.79999995 reward: 48.47999999999999                       blocks_per_halving: 567240
# good max_supply found: 109999099.99999994 reward: 50.499999999999986                       blocks_per_halving: 544550
# good max_supply found: 109999099.99999994 reward: 50.499999999999986                       blocks_per_halving: 544550
# good max_supply found: 109999099.99999994 reward: 50.499999999999986                       blocks_per_halving: 544550
# good max_supply found: 109999099.99999994 reward: 50.499999999999986                       blocks_per_halving: 544550
# good max_supply found: 109999988.79999992 reward: 52.51999999999998                       blocks_per_halving: 523610
# good max_supply found: 109999988.79999992 reward: 52.51999999999998                       blocks_per_halving: 523610
# good max_supply found: 109999988.79999992 reward: 52.51999999999998                       blocks_per_halving: 523610
# good max_supply found: 109999988.79999992 reward: 52.51999999999998                       blocks_per_halving: 523610
# good max_supply found: 109999867.59999995 reward: 53.52999999999998                       blocks_per_halving: 513730
# good max_supply found: 109999867.59999995 reward: 53.52999999999998                       blocks_per_halving: 513730
# good max_supply found: 109999867.59999995 reward: 53.52999999999998                       blocks_per_halving: 513730
# good max_supply found: 109999867.59999995 reward: 53.52999999999998                       blocks_per_halving: 513730
# good max_supply found: 109999180.7999999 reward: 58.57999999999997                       blocks_per_halving: 469440
# good max_supply found: 109999180.7999999 reward: 58.57999999999997                       blocks_per_halving: 469440
# good max_supply found: 109999180.7999999 reward: 58.57999999999997                       blocks_per_halving: 469440
# good max_supply found: 109999180.7999999 reward: 58.57999999999997                       blocks_per_halving: 469440
# good max_supply found: 109999180.79999988 reward: 64.63999999999996                       blocks_per_halving: 425430
# good max_supply found: 109999180.79999988 reward: 64.63999999999996                       blocks_per_halving: 425430
# good max_supply found: 109999180.79999988 reward: 64.63999999999996                       blocks_per_halving: 425430
# good max_supply found: 109999180.79999988 reward: 64.63999999999996                       blocks_per_halving: 425430
# good max_supply found: 109999665.59999992 reward: 66.65999999999997                       blocks_per_halving: 412540
# good max_supply found: 109999665.59999992 reward: 66.65999999999997                       blocks_per_halving: 412540
# good max_supply found: 109999665.59999992 reward: 66.65999999999997                       blocks_per_halving: 412540
# good max_supply found: 109999665.59999992 reward: 66.65999999999997                       blocks_per_halving: 412540
# good max_supply found: 109999180.79999995 reward: 72.72                       blocks_per_halving: 378160
# good max_supply found: 109999180.79999995 reward: 72.72                       blocks_per_halving: 378160
# good max_supply found: 109999180.79999995 reward: 72.72                       blocks_per_halving: 378160
# good max_supply found: 109999180.79999995 reward: 72.72                       blocks_per_halving: 378160
# good max_supply found: 109999261.59999993 reward: 73.73                       blocks_per_halving: 372980
# good max_supply found: 109999261.59999993 reward: 73.73                       blocks_per_halving: 372980
# good max_supply found: 109999261.59999993 reward: 73.73                       blocks_per_halving: 372980
# good max_supply found: 109999261.59999993 reward: 73.73                       blocks_per_halving: 372980
# good max_supply found: 109999342.39999995 reward: 74.74000000000001                       blocks_per_halving: 367940
# good max_supply found: 109999342.39999995 reward: 74.74000000000001                       blocks_per_halving: 367940
# good max_supply found: 109999342.39999995 reward: 74.74000000000001                       blocks_per_halving: 367940
# good max_supply found: 109999342.39999995 reward: 74.74000000000001                       blocks_per_halving: 367940
# good max_supply found: 109999504.00000001 reward: 86.86000000000007                       blocks_per_halving: 316600
# good max_supply found: 109999504.00000001 reward: 86.86000000000007                       blocks_per_halving: 316600
# good max_supply found: 109999504.00000001 reward: 86.86000000000007                       blocks_per_halving: 316600
# good max_supply found: 109999504.00000001 reward: 86.86000000000007                       blocks_per_halving: 316600
# good max_supply found: 109999180.80000004 reward: 87.87000000000008                       blocks_per_halving: 312960
# good max_supply found: 109999180.80000004 reward: 87.87000000000008                       blocks_per_halving: 312960
# good max_supply found: 109999180.80000004 reward: 87.87000000000008                       blocks_per_halving: 312960
# good max_supply found: 109999180.80000004 reward: 87.87000000000008                       blocks_per_halving: 312960
# good max_supply found: 109999908.00000007 reward: 90.90000000000009                       blocks_per_halving: 302530
# good max_supply found: 109999908.00000007 reward: 90.90000000000009                       blocks_per_halving: 302530
# good max_supply found: 109999908.00000007 reward: 90.90000000000009                       blocks_per_halving: 302530
# good max_supply found: 109999908.00000007 reward: 90.90000000000009                       blocks_per_halving: 302530
# good max_supply found: 209999644.40000024 reward: 91.9100000000001                       blocks_per_halving: 571210
# good max_supply found: 209999644.40000024 reward: 91.9100000000001                       blocks_per_halving: 571210
# good max_supply found: 209999644.40000024 reward: 91.9100000000001                       blocks_per_halving: 571210
# good max_supply found: 209999644.40000024 reward: 91.9100000000001                       blocks_per_halving: 571210
# good max_supply found: 209999200.00000018 reward: 92.9200000000001                       blocks_per_halving: 565000
# good max_supply found: 209999200.00000018 reward: 92.9200000000001                       blocks_per_halving: 565000
# good max_supply found: 209999200.00000018 reward: 92.9200000000001                       blocks_per_halving: 565000
# good max_supply found: 209999200.00000018 reward: 92.9200000000001                       blocks_per_halving: 565000
# good max_supply found: 109999544.40000002 reward: 93.9300000000001                       blocks_per_halving: 292770
# good max_supply found: 109999544.40000002 reward: 93.9300000000001                       blocks_per_halving: 292770
# good max_supply found: 109999544.40000002 reward: 93.9300000000001                       blocks_per_halving: 292770
# good max_supply found: 109999544.40000002 reward: 93.9300000000001                       blocks_per_halving: 292770
# good max_supply found: 209999684.80000013 reward: 94.94000000000011                       blocks_per_halving: 552980
# good max_supply found: 209999684.80000013 reward: 94.94000000000011                       blocks_per_halving: 552980
# good max_supply found: 209999684.80000013 reward: 94.94000000000011                       blocks_per_halving: 552980
# good max_supply found: 209999684.80000013 reward: 94.94000000000011                       blocks_per_halving: 552980
# good max_supply found: 109999180.80000007 reward: 96.96000000000012                       blocks_per_halving: 283620
# good max_supply found: 109999180.80000007 reward: 96.96000000000012                       blocks_per_halving: 283620
# good max_supply found: 109999180.80000007 reward: 96.96000000000012                       blocks_per_halving: 283620
# good max_supply found: 109999180.80000007 reward: 96.96000000000012                       blocks_per_halving: 283620
# good max_supply found: 209999846.4000003 reward: 96.96000000000012                       blocks_per_halving: 541460
# good max_supply found: 209999846.4000003 reward: 96.96000000000012                       blocks_per_halving: 541460
# good max_supply found: 209999846.4000003 reward: 96.96000000000012                       blocks_per_halving: 541460
# good max_supply found: 209999846.4000003 reward: 96.96000000000012                       blocks_per_halving: 541460
# good max_supply found: 209999927.20000032 reward: 98.98000000000013                       blocks_per_halving: 530410
# good max_supply found: 209999927.20000032 reward: 98.98000000000013                       blocks_per_halving: 530410
# good max_supply found: 209999927.20000032 reward: 98.98000000000013                       blocks_per_halving: 530410
# good max_supply found: 209999927.20000032 reward: 98.98000000000013                       blocks_per_halving: 530410
# good max_supply found: 209999200.0000003 reward: 101.00000000000014                       blocks_per_halving: 519800
# good max_supply found: 209999200.0000003 reward: 101.00000000000014                       blocks_per_halving: 519800
# good max_supply found: 209999200.0000003 reward: 101.00000000000014                       blocks_per_halving: 519800
# good max_supply found: 209999200.0000003 reward: 101.00000000000014                       blocks_per_halving: 519800
# good max_supply found: 109999423.20000012 reward: 102.01000000000015                       blocks_per_halving: 269580
# good max_supply found: 109999423.20000012 reward: 102.01000000000015                       blocks_per_halving: 269580
# good max_supply found: 109999423.20000012 reward: 102.01000000000015                       blocks_per_halving: 269580
# good max_supply found: 109999423.20000012 reward: 102.01000000000015                       blocks_per_halving: 269580
# good max_supply found: 209999119.2000004 reward: 104.03000000000016                       blocks_per_halving: 504660
# good max_supply found: 209999119.2000004 reward: 104.03000000000016                       blocks_per_halving: 504660
# good max_supply found: 209999119.2000004 reward: 104.03000000000016                       blocks_per_halving: 504660
# good max_supply found: 209999119.2000004 reward: 104.03000000000016                       blocks_per_halving: 504660
# good max_supply found: 109999302.00000007 reward: 106.05000000000017                       blocks_per_halving: 259310
# good max_supply found: 109999302.00000007 reward: 106.05000000000017                       blocks_per_halving: 259310
# good max_supply found: 109999302.00000007 reward: 106.05000000000017                       blocks_per_halving: 259310
# good max_supply found: 109999302.00000007 reward: 106.05000000000017                       blocks_per_halving: 259310
# good max_supply found: 209999967.60000053 reward: 112.1100000000002                       blocks_per_halving: 468290
# good max_supply found: 209999967.60000053 reward: 112.1100000000002                       blocks_per_halving: 468290
# good max_supply found: 209999967.60000053 reward: 112.1100000000002                       blocks_per_halving: 468290
# good max_supply found: 209999967.60000053 reward: 112.1100000000002                       blocks_per_halving: 468290
# good max_supply found: 209999200.00000036 reward: 114.13000000000021                       blocks_per_halving: 460000
# good max_supply found: 209999200.00000036 reward: 114.13000000000021                       blocks_per_halving: 460000
# good max_supply found: 209999200.00000036 reward: 114.13000000000021                       blocks_per_halving: 460000
# good max_supply found: 209999200.00000036 reward: 114.13000000000021                       blocks_per_halving: 460000
# good max_supply found: 209999200.00000036 reward: 116.15000000000022                       blocks_per_halving: 452000
# good max_supply found: 209999200.00000036 reward: 116.15000000000022                       blocks_per_halving: 452000
# good max_supply found: 209999200.00000036 reward: 116.15000000000022                       blocks_per_halving: 452000
# good max_supply found: 209999200.00000036 reward: 116.15000000000022                       blocks_per_halving: 452000
# good max_supply found: 109999180.80000018 reward: 117.16000000000022                       blocks_per_halving: 234720
# good max_supply found: 109999180.80000018 reward: 117.16000000000022                       blocks_per_halving: 234720
# good max_supply found: 109999180.80000018 reward: 117.16000000000022                       blocks_per_halving: 234720
# good max_supply found: 109999180.80000018 reward: 117.16000000000022                       blocks_per_halving: 234720
# good max_supply found: 209999927.20000044 reward: 119.18000000000023                       blocks_per_halving: 440510
# good max_supply found: 209999927.20000044 reward: 119.18000000000023                       blocks_per_halving: 440510
# good max_supply found: 209999927.20000044 reward: 119.18000000000023                       blocks_per_halving: 440510
# good max_supply found: 209999927.20000044 reward: 119.18000000000023                       blocks_per_halving: 440510
# good max_supply found: 109999100.00000016 reward: 126.25000000000027                       blocks_per_halving: 217820
# good max_supply found: 109999100.00000016 reward: 126.25000000000027                       blocks_per_halving: 217820
# good max_supply found: 109999100.00000016 reward: 126.25000000000027                       blocks_per_halving: 217820
# good max_supply found: 109999100.00000016 reward: 126.25000000000027                       blocks_per_halving: 217820
# good max_supply found: 209999200.0000004 reward: 126.25000000000027                       blocks_per_halving: 415840
# good max_supply found: 209999200.0000004 reward: 126.25000000000027                       blocks_per_halving: 415840
# good max_supply found: 209999200.0000004 reward: 126.25000000000027                       blocks_per_halving: 415840
# good max_supply found: 209999200.0000004 reward: 126.25000000000027                       blocks_per_halving: 415840
# good max_supply found: 209999361.60000032 reward: 127.26000000000028                       blocks_per_halving: 412540
# good max_supply found: 209999361.60000032 reward: 127.26000000000028                       blocks_per_halving: 412540
# good max_supply found: 209999361.60000032 reward: 127.26000000000028                       blocks_per_halving: 412540
# good max_supply found: 209999361.60000032 reward: 127.26000000000028                       blocks_per_halving: 412540
# good max_supply found: 109999221.20000017 reward: 128.27000000000027                       blocks_per_halving: 214390
# good max_supply found: 109999221.20000017 reward: 128.27000000000027                       blocks_per_halving: 214390
# good max_supply found: 109999221.20000017 reward: 128.27000000000027                       blocks_per_halving: 214390
# good max_supply found: 109999221.20000017 reward: 128.27000000000027                       blocks_per_halving: 214390
# good max_supply found: 309999300.0000004 reward: 131.30000000000024                       blocks_per_halving: 590250
# good max_supply found: 309999300.0000004 reward: 131.30000000000024                       blocks_per_halving: 590250
# good max_supply found: 309999300.0000004 reward: 131.30000000000024                       blocks_per_halving: 590250
# good max_supply found: 309999300.0000004 reward: 131.30000000000024                       blocks_per_halving: 590250
# good max_supply found: 109999665.60000014 reward: 133.32000000000022                       blocks_per_halving: 206270
# good max_supply found: 109999665.60000014 reward: 133.32000000000022                       blocks_per_halving: 206270
# good max_supply found: 109999665.60000014 reward: 133.32000000000022                       blocks_per_halving: 206270
# good max_supply found: 109999665.60000014 reward: 133.32000000000022                       blocks_per_halving: 206270
# good max_supply found: 309999906.0000002 reward: 136.3500000000002                       blocks_per_halving: 568390
# good max_supply found: 309999906.0000002 reward: 136.3500000000002                       blocks_per_halving: 568390
# good max_supply found: 309999906.0000002 reward: 136.3500000000002                       blocks_per_halving: 568390
# good max_supply found: 309999906.0000002 reward: 136.3500000000002                       blocks_per_halving: 568390
# good max_supply found: 309999542.4000004 reward: 137.36000000000018                       blocks_per_halving: 564210
# good max_supply found: 309999542.4000004 reward: 137.36000000000018                       blocks_per_halving: 564210
# good max_supply found: 309999542.4000004 reward: 137.36000000000018                       blocks_per_halving: 564210
# good max_supply found: 309999542.4000004 reward: 137.36000000000018                       blocks_per_halving: 564210
# good max_supply found: 309999704.0000003 reward: 141.40000000000015                       blocks_per_halving: 548090
# good max_supply found: 309999704.0000003 reward: 141.40000000000015                       blocks_per_halving: 548090
# good max_supply found: 309999704.0000003 reward: 141.40000000000015                       blocks_per_halving: 548090
# good max_supply found: 309999704.0000003 reward: 141.40000000000015                       blocks_per_halving: 548090
# good max_supply found: 309999461.60000014 reward: 143.42000000000013                       blocks_per_halving: 540370
# good max_supply found: 309999461.60000014 reward: 143.42000000000013                       blocks_per_halving: 540370
# good max_supply found: 309999461.60000014 reward: 143.42000000000013                       blocks_per_halving: 540370
# good max_supply found: 309999461.60000014 reward: 143.42000000000013                       blocks_per_halving: 540370
# good max_supply found: 109999180.80000004 reward: 145.4400000000001                       blocks_per_halving: 189080
# good max_supply found: 109999180.80000004 reward: 145.4400000000001                       blocks_per_halving: 189080
# good max_supply found: 109999180.80000004 reward: 145.4400000000001                       blocks_per_halving: 189080
# good max_supply found: 109999180.80000004 reward: 145.4400000000001                       blocks_per_halving: 189080
# good max_supply found: 309999502.0 reward: 146.4500000000001                       blocks_per_halving: 529190
# good max_supply found: 309999502.0 reward: 146.4500000000001                       blocks_per_halving: 529190
# good max_supply found: 309999502.0 reward: 146.4500000000001                       blocks_per_halving: 529190
# good max_supply found: 309999502.0 reward: 146.4500000000001                       blocks_per_halving: 529190
# good max_supply found: 109999261.6 reward: 147.4600000000001                       blocks_per_halving: 186490
# good max_supply found: 109999261.6 reward: 147.4600000000001                       blocks_per_halving: 186490
# good max_supply found: 109999261.6 reward: 147.4600000000001                       blocks_per_halving: 186490
# good max_supply found: 109999261.6 reward: 147.4600000000001                       blocks_per_halving: 186490
# good max_supply found: 309999421.1999999 reward: 148.47000000000008                       blocks_per_halving: 521990
# good max_supply found: 309999421.1999999 reward: 148.47000000000008                       blocks_per_halving: 521990
# good max_supply found: 309999421.1999999 reward: 148.47000000000008                       blocks_per_halving: 521990
# good max_supply found: 309999421.1999999 reward: 148.47000000000008                       blocks_per_halving: 521990
# good max_supply found: 109999342.39999999 reward: 149.48000000000008                       blocks_per_halving: 183970
# good max_supply found: 109999342.39999999 reward: 149.48000000000008                       blocks_per_halving: 183970
# good max_supply found: 109999342.39999999 reward: 149.48000000000008                       blocks_per_halving: 183970
# good max_supply found: 109999342.39999999 reward: 149.48000000000008                       blocks_per_halving: 183970
# good max_supply found: 209999765.6 reward: 150.49000000000007                       blocks_per_halving: 348860
# good max_supply found: 209999765.6 reward: 150.49000000000007                       blocks_per_halving: 348860
# good max_supply found: 209999765.6 reward: 150.49000000000007                       blocks_per_halving: 348860
# good max_supply found: 209999765.6 reward: 150.49000000000007                       blocks_per_halving: 348860
# good max_supply found: 309999300.0 reward: 151.50000000000006                       blocks_per_halving: 511550
# good max_supply found: 309999300.0 reward: 151.50000000000006                       blocks_per_halving: 511550
# good max_supply found: 309999300.0 reward: 151.50000000000006                       blocks_per_halving: 511550
# good max_supply found: 309999300.0 reward: 151.50000000000006                       blocks_per_halving: 511550
# good max_supply found: 309999865.6 reward: 153.52000000000004                       blocks_per_halving: 504820
# good max_supply found: 309999865.6 reward: 153.52000000000004                       blocks_per_halving: 504820
# good max_supply found: 309999865.6 reward: 153.52000000000004                       blocks_per_halving: 504820
# good max_supply found: 309999865.6 reward: 153.52000000000004                       blocks_per_halving: 504820
# good max_supply found: 309999542.4 reward: 154.53000000000003                       blocks_per_halving: 501520
# good max_supply found: 309999542.4 reward: 154.53000000000003                       blocks_per_halving: 501520
# good max_supply found: 309999542.4 reward: 154.53000000000003                       blocks_per_halving: 501520
# good max_supply found: 309999542.4 reward: 154.53000000000003                       blocks_per_halving: 501520
# good max_supply found: 309999703.99999994 reward: 162.60999999999996                       blocks_per_halving: 476600
# good max_supply found: 309999703.99999994 reward: 162.60999999999996                       blocks_per_halving: 476600
# good max_supply found: 309999703.99999994 reward: 162.60999999999996                       blocks_per_halving: 476600
# good max_supply found: 309999703.99999994 reward: 162.60999999999996                       blocks_per_halving: 476600
# good max_supply found: 109999180.79999992 reward: 164.62999999999994                       blocks_per_halving: 167040
# good max_supply found: 109999180.79999992 reward: 164.62999999999994                       blocks_per_halving: 167040
# good max_supply found: 109999180.79999992 reward: 164.62999999999994                       blocks_per_halving: 167040
# good max_supply found: 109999180.79999992 reward: 164.62999999999994                       blocks_per_halving: 167040
# good max_supply found: 109999827.19999991 reward: 168.6699999999999                       blocks_per_halving: 163040
# good max_supply found: 109999827.19999991 reward: 168.6699999999999                       blocks_per_halving: 163040
# good max_supply found: 109999827.19999991 reward: 168.6699999999999                       blocks_per_halving: 163040
# good max_supply found: 109999827.19999991 reward: 168.6699999999999                       blocks_per_halving: 163040
# good max_supply found: 109999463.59999987 reward: 170.68999999999988                       blocks_per_halving: 161110
# good max_supply found: 109999463.59999987 reward: 170.68999999999988                       blocks_per_halving: 161110
# good max_supply found: 109999463.59999987 reward: 170.68999999999988                       blocks_per_halving: 161110
# good max_supply found: 109999463.59999987 reward: 170.68999999999988                       blocks_per_halving: 161110
# good max_supply found: 409999723.1999996 reward: 172.70999999999987                       blocks_per_halving: 593480
# good max_supply found: 409999723.1999996 reward: 172.70999999999987                       blocks_per_halving: 593480
# good max_supply found: 409999723.1999996 reward: 172.70999999999987                       blocks_per_halving: 593480
# good max_supply found: 409999723.1999996 reward: 172.70999999999987                       blocks_per_halving: 593480
# good max_supply found: 109999503.9999999 reward: 173.71999999999986                       blocks_per_halving: 158300
# good max_supply found: 109999503.9999999 reward: 173.71999999999986                       blocks_per_halving: 158300
# good max_supply found: 109999503.9999999 reward: 173.71999999999986                       blocks_per_halving: 158300
# good max_supply found: 109999503.9999999 reward: 173.71999999999986                       blocks_per_halving: 158300
# good max_supply found: 209999684.79999974 reward: 173.71999999999986                       blocks_per_halving: 302210
# good max_supply found: 209999684.79999974 reward: 173.71999999999986                       blocks_per_halving: 302210
# good max_supply found: 209999684.79999974 reward: 173.71999999999986                       blocks_per_halving: 302210
# good max_supply found: 209999684.79999974 reward: 173.71999999999986                       blocks_per_halving: 302210
# good max_supply found: 309999865.59999967 reward: 173.71999999999986                       blocks_per_halving: 446120
# good max_supply found: 309999865.59999967 reward: 173.71999999999986                       blocks_per_halving: 446120
# good max_supply found: 309999865.59999967 reward: 173.71999999999986                       blocks_per_halving: 446120
# good max_supply found: 309999865.59999967 reward: 173.71999999999986                       blocks_per_halving: 446120
# good max_supply found: 109999180.79999986 reward: 175.73999999999984                       blocks_per_halving: 156480
# good max_supply found: 109999180.79999986 reward: 175.73999999999984                       blocks_per_halving: 156480
# good max_supply found: 109999180.79999986 reward: 175.73999999999984                       blocks_per_halving: 156480
# good max_supply found: 109999180.79999986 reward: 175.73999999999984                       blocks_per_halving: 156480
# good max_supply found: 309999219.19999975 reward: 177.75999999999982                       blocks_per_halving: 435980
# good max_supply found: 309999219.19999975 reward: 177.75999999999982                       blocks_per_halving: 435980
# good max_supply found: 309999219.19999975 reward: 177.75999999999982                       blocks_per_halving: 435980
# good max_supply found: 309999219.19999975 reward: 177.75999999999982                       blocks_per_halving: 435980
# good max_supply found: 409999884.7999994 reward: 177.75999999999982                       blocks_per_halving: 576620
# good max_supply found: 409999884.7999994 reward: 177.75999999999982                       blocks_per_halving: 576620
# good max_supply found: 409999884.7999994 reward: 177.75999999999982                       blocks_per_halving: 576620
# good max_supply found: 409999884.7999994 reward: 177.75999999999982                       blocks_per_halving: 576620
# good max_supply found: 409999076.79999965 reward: 179.7799999999998                       blocks_per_halving: 570140
# good max_supply found: 409999076.79999965 reward: 179.7799999999998                       blocks_per_halving: 570140
# good max_supply found: 409999076.79999965 reward: 179.7799999999998                       blocks_per_halving: 570140
# good max_supply found: 409999076.79999965 reward: 179.7799999999998                       blocks_per_halving: 570140
# good max_supply found: 109999867.59999986 reward: 180.7899999999998                       blocks_per_halving: 152110
# good max_supply found: 109999867.59999986 reward: 180.7899999999998                       blocks_per_halving: 152110
# good max_supply found: 109999867.59999986 reward: 180.7899999999998                       blocks_per_halving: 152110
# good max_supply found: 109999867.59999986 reward: 180.7899999999998                       blocks_per_halving: 152110
# good max_supply found: 409999480.7999995 reward: 183.81999999999977                       blocks_per_halving: 557610
# good max_supply found: 409999480.7999995 reward: 183.81999999999977                       blocks_per_halving: 557610
# good max_supply found: 409999480.7999995 reward: 183.81999999999977                       blocks_per_halving: 557610
# good max_supply found: 409999480.7999995 reward: 183.81999999999977                       blocks_per_halving: 557610
# good max_supply found: 209999199.9999998 reward: 185.83999999999975                       blocks_per_halving: 282500
# good max_supply found: 209999199.9999998 reward: 185.83999999999975                       blocks_per_halving: 282500
# good max_supply found: 209999199.9999998 reward: 185.83999999999975                       blocks_per_halving: 282500
# good max_supply found: 209999199.9999998 reward: 185.83999999999975                       blocks_per_halving: 282500
# good max_supply found: 309999097.9999996 reward: 186.84999999999974                       blocks_per_halving: 414770
# good max_supply found: 309999097.9999996 reward: 186.84999999999974                       blocks_per_halving: 414770
# good max_supply found: 309999097.9999996 reward: 186.84999999999974                       blocks_per_halving: 414770
# good max_supply found: 309999097.9999996 reward: 186.84999999999974                       blocks_per_halving: 414770
# good max_supply found: 309999057.5999996 reward: 187.85999999999973                       blocks_per_halving: 412540
# good max_supply found: 309999057.5999996 reward: 187.85999999999973                       blocks_per_halving: 412540
# good max_supply found: 309999057.5999996 reward: 187.85999999999973                       blocks_per_halving: 412540
# good max_supply found: 309999057.5999996 reward: 187.85999999999973                       blocks_per_halving: 412540
# good max_supply found: 209999684.79999954 reward: 189.8799999999997                       blocks_per_halving: 276490
# good max_supply found: 209999684.79999954 reward: 189.8799999999997                       blocks_per_halving: 276490
# good max_supply found: 209999684.79999954 reward: 189.8799999999997                       blocks_per_halving: 276490
# good max_supply found: 209999684.79999954 reward: 189.8799999999997                       blocks_per_halving: 276490
# good max_supply found: 109999180.79999979 reward: 193.91999999999967                       blocks_per_halving: 141810
# good max_supply found: 109999180.79999979 reward: 193.91999999999967                       blocks_per_halving: 141810
# good max_supply found: 109999180.79999979 reward: 193.91999999999967                       blocks_per_halving: 141810
# good max_supply found: 109999180.79999979 reward: 193.91999999999967                       blocks_per_halving: 141810
# good max_supply found: 209999846.39999968 reward: 193.91999999999967                       blocks_per_halving: 270730
# good max_supply found: 209999846.39999968 reward: 193.91999999999967                       blocks_per_halving: 270730
# good max_supply found: 209999846.39999968 reward: 193.91999999999967                       blocks_per_halving: 270730
# good max_supply found: 209999846.39999968 reward: 193.91999999999967                       blocks_per_halving: 270730
# good max_supply found: 309999299.99999946 reward: 196.94999999999965                       blocks_per_halving: 393500
# good max_supply found: 309999299.99999946 reward: 196.94999999999965                       blocks_per_halving: 393500
# good max_supply found: 309999299.99999946 reward: 196.94999999999965                       blocks_per_halving: 393500
# good max_supply found: 309999299.99999946 reward: 196.94999999999965                       blocks_per_halving: 393500
# good max_supply found: 209999199.99999964 reward: 201.9999999999996                       blocks_per_halving: 259900
# good max_supply found: 209999199.99999964 reward: 201.9999999999996                       blocks_per_halving: 259900
# good max_supply found: 209999199.99999964 reward: 201.9999999999996                       blocks_per_halving: 259900
# good max_supply found: 209999199.99999964 reward: 201.9999999999996                       blocks_per_halving: 259900
# good max_supply found: 109999423.19999975 reward: 204.01999999999958                       blocks_per_halving: 134790
# good max_supply found: 109999423.19999975 reward: 204.01999999999958                       blocks_per_halving: 134790
# good max_supply found: 109999423.19999975 reward: 204.01999999999958                       blocks_per_halving: 134790
# good max_supply found: 109999423.19999975 reward: 204.01999999999958                       blocks_per_halving: 134790
# good max_supply found: 209999927.1999995 reward: 205.02999999999957                       blocks_per_halving: 256060
# good max_supply found: 209999927.1999995 reward: 205.02999999999957                       blocks_per_halving: 256060
# good max_supply found: 209999927.1999995 reward: 205.02999999999957                       blocks_per_halving: 256060
# good max_supply found: 209999927.1999995 reward: 205.02999999999957                       blocks_per_halving: 256060
# good max_supply found: 309999542.3999993 reward: 206.03999999999957                       blocks_per_halving: 376140
# good max_supply found: 309999542.3999993 reward: 206.03999999999957                       blocks_per_halving: 376140
# good max_supply found: 309999542.3999993 reward: 206.03999999999957                       blocks_per_halving: 376140
# good max_supply found: 309999542.3999993 reward: 206.03999999999957                       blocks_per_halving: 376140
# good max_supply found: 209999119.19999957 reward: 208.05999999999955                       blocks_per_halving: 252330
# good max_supply found: 209999119.19999957 reward: 208.05999999999955                       blocks_per_halving: 252330
# good max_supply found: 209999119.19999957 reward: 208.05999999999955                       blocks_per_halving: 252330
# good max_supply found: 209999119.19999957 reward: 208.05999999999955                       blocks_per_halving: 252330
# good max_supply found: 509999580.7999989 reward: 214.1199999999995                       blocks_per_halving: 595460
# good max_supply found: 509999580.7999989 reward: 214.1199999999995                       blocks_per_halving: 595460
# good max_supply found: 509999580.7999989 reward: 214.1199999999995                       blocks_per_halving: 595460
# good max_supply found: 509999580.7999989 reward: 214.1199999999995                       blocks_per_halving: 595460
# good max_supply found: 109999503.99999972 reward: 217.14999999999947                       blocks_per_halving: 126640
# good max_supply found: 109999503.99999972 reward: 217.14999999999947                       blocks_per_halving: 126640
# good max_supply found: 109999503.99999972 reward: 217.14999999999947                       blocks_per_halving: 126640
# good max_supply found: 109999503.99999972 reward: 217.14999999999947                       blocks_per_halving: 126640
# good max_supply found: 209999927.19999945 reward: 219.16999999999945                       blocks_per_halving: 239540
# good max_supply found: 209999927.19999945 reward: 219.16999999999945                       blocks_per_halving: 239540
# good max_supply found: 209999927.19999945 reward: 219.16999999999945                       blocks_per_halving: 239540
# good max_supply found: 209999927.19999945 reward: 219.16999999999945                       blocks_per_halving: 239540
# good max_supply found: 509999823.1999986 reward: 219.16999999999945                       blocks_per_halving: 581740
# good max_supply found: 509999823.1999986 reward: 219.16999999999945                       blocks_per_halving: 581740
# good max_supply found: 509999823.1999986 reward: 219.16999999999945                       blocks_per_halving: 581740
# good max_supply found: 509999823.1999986 reward: 219.16999999999945                       blocks_per_halving: 581740
# good max_supply found: 509999136.3999987 reward: 223.2099999999994                       blocks_per_halving: 571210
# good max_supply found: 509999136.3999987 reward: 223.2099999999994                       blocks_per_halving: 571210
# good max_supply found: 509999136.3999987 reward: 223.2099999999994                       blocks_per_halving: 571210
# good max_supply found: 509999136.3999987 reward: 223.2099999999994                       blocks_per_halving: 571210
# good max_supply found: 409999723.1999989 reward: 224.2199999999994                       blocks_per_halving: 457140
# good max_supply found: 409999723.1999989 reward: 224.2199999999994                       blocks_per_halving: 457140
# good max_supply found: 409999723.1999989 reward: 224.2199999999994                       blocks_per_halving: 457140
# good max_supply found: 409999723.1999989 reward: 224.2199999999994                       blocks_per_halving: 457140
# good max_supply found: 409999682.79999906 reward: 225.2299999999994                       blocks_per_halving: 455090
# good max_supply found: 409999682.79999906 reward: 225.2299999999994                       blocks_per_halving: 455090
# good max_supply found: 409999682.79999906 reward: 225.2299999999994                       blocks_per_halving: 455090
# good max_supply found: 409999682.79999906 reward: 225.2299999999994                       blocks_per_halving: 455090
# good max_supply found: 509999257.5999987 reward: 226.23999999999938                       blocks_per_halving: 563560
# good max_supply found: 509999257.5999987 reward: 226.23999999999938                       blocks_per_halving: 563560
# good max_supply found: 509999257.5999987 reward: 226.23999999999938                       blocks_per_halving: 563560
# good max_supply found: 509999257.5999987 reward: 226.23999999999938                       blocks_per_halving: 563560
# good max_supply found: 209999199.9999995 reward: 228.25999999999937                       blocks_per_halving: 230000
# good max_supply found: 209999199.9999995 reward: 228.25999999999937                       blocks_per_halving: 230000
# good max_supply found: 209999199.9999995 reward: 228.25999999999937                       blocks_per_halving: 230000
# good max_supply found: 209999199.9999995 reward: 228.25999999999937                       blocks_per_halving: 230000
# good max_supply found: 409999723.1999988 reward: 230.27999999999935                       blocks_per_halving: 445110
# good max_supply found: 409999723.1999988 reward: 230.27999999999935                       blocks_per_halving: 445110
# good max_supply found: 409999723.1999988 reward: 230.27999999999935                       blocks_per_halving: 445110
# good max_supply found: 409999723.1999988 reward: 230.27999999999935                       blocks_per_halving: 445110
# good max_supply found: 209999199.99999943 reward: 232.29999999999933                       blocks_per_halving: 226000
# good max_supply found: 209999199.99999943 reward: 232.29999999999933                       blocks_per_halving: 226000
# good max_supply found: 209999199.99999943 reward: 232.29999999999933                       blocks_per_halving: 226000
# good max_supply found: 209999199.99999943 reward: 232.29999999999933                       blocks_per_halving: 226000
# good max_supply found: 309999703.99999917 reward: 232.29999999999933                       blocks_per_halving: 333620
# good max_supply found: 309999703.99999917 reward: 232.29999999999933                       blocks_per_halving: 333620
# good max_supply found: 309999703.99999917 reward: 232.29999999999933                       blocks_per_halving: 333620
# good max_supply found: 309999703.99999917 reward: 232.29999999999933                       blocks_per_halving: 333620
# good max_supply found: 109999180.79999962 reward: 234.3199999999993                       blocks_per_halving: 117360
# good max_supply found: 109999180.79999962 reward: 234.3199999999993                       blocks_per_halving: 117360
# good max_supply found: 109999180.79999962 reward: 234.3199999999993                       blocks_per_halving: 117360
# good max_supply found: 109999180.79999962 reward: 234.3199999999993                       blocks_per_halving: 117360
# good max_supply found: 209999078.7999994 reward: 235.3299999999993                       blocks_per_halving: 223090
# good max_supply found: 209999078.7999994 reward: 235.3299999999993                       blocks_per_halving: 223090
# good max_supply found: 209999078.7999994 reward: 235.3299999999993                       blocks_per_halving: 223090
# good max_supply found: 209999078.7999994 reward: 235.3299999999993                       blocks_per_halving: 223090
# good max_supply found: 509999823.1999985 reward: 240.37999999999926                       blocks_per_halving: 530410
# good max_supply found: 509999823.1999985 reward: 240.37999999999926                       blocks_per_halving: 530410
# good max_supply found: 509999823.1999985 reward: 240.37999999999926                       blocks_per_halving: 530410
# good max_supply found: 509999823.1999985 reward: 240.37999999999926                       blocks_per_halving: 530410
# good max_supply found: 209999644.39999938 reward: 241.38999999999925                       blocks_per_halving: 217490
# good max_supply found: 209999644.39999938 reward: 241.38999999999925                       blocks_per_halving: 217490
# good max_supply found: 209999644.39999938 reward: 241.38999999999925                       blocks_per_halving: 217490
# good max_supply found: 209999644.39999938 reward: 241.38999999999925                       blocks_per_halving: 217490
# good max_supply found: 509999136.39999855 reward: 241.38999999999925                       blocks_per_halving: 528190
# good max_supply found: 509999136.39999855 reward: 241.38999999999925                       blocks_per_halving: 528190
# good max_supply found: 509999136.39999855 reward: 241.38999999999925                       blocks_per_halving: 528190
# good max_supply found: 509999136.39999855 reward: 241.38999999999925                       blocks_per_halving: 528190
# good max_supply found: 509999903.99999857 reward: 242.39999999999924                       blocks_per_halving: 525990
# good max_supply found: 509999903.99999857 reward: 242.39999999999924                       blocks_per_halving: 525990
# good max_supply found: 509999903.99999857 reward: 242.39999999999924                       blocks_per_halving: 525990
# good max_supply found: 509999903.99999857 reward: 242.39999999999924                       blocks_per_halving: 525990
# good max_supply found: 409999803.9999984 reward: 243.40999999999923                       blocks_per_halving: 421100
# good max_supply found: 409999803.9999984 reward: 243.40999999999923                       blocks_per_halving: 421100
# good max_supply found: 409999803.9999984 reward: 243.40999999999923                       blocks_per_halving: 421100
# good max_supply found: 409999803.9999984 reward: 243.40999999999923                       blocks_per_halving: 421100
# good max_supply found: 409999884.7999984 reward: 244.41999999999922                       blocks_per_halving: 419360
# good max_supply found: 409999884.7999984 reward: 244.41999999999922                       blocks_per_halving: 419360
# good max_supply found: 409999884.7999984 reward: 244.41999999999922                       blocks_per_halving: 419360
# good max_supply found: 409999884.7999984 reward: 244.41999999999922                       blocks_per_halving: 419360
# good max_supply found: 209999725.19999936 reward: 245.4299999999992                       blocks_per_halving: 213910
# good max_supply found: 209999725.19999936 reward: 245.4299999999992                       blocks_per_halving: 213910
# good max_supply found: 209999725.19999936 reward: 245.4299999999992                       blocks_per_halving: 213910
# good max_supply found: 209999725.19999936 reward: 245.4299999999992                       blocks_per_halving: 213910
# good max_supply found: 409999117.1999984 reward: 251.48999999999916                       blocks_per_halving: 407570
# good max_supply found: 409999117.1999984 reward: 251.48999999999916                       blocks_per_halving: 407570
# good max_supply found: 409999117.1999984 reward: 251.48999999999916                       blocks_per_halving: 407570
# good max_supply found: 409999117.1999984 reward: 251.48999999999916                       blocks_per_halving: 407570
# good max_supply found: 109999099.99999961 reward: 252.49999999999915                       blocks_per_halving: 108910
# good max_supply found: 109999099.99999961 reward: 252.49999999999915                       blocks_per_halving: 108910
# good max_supply found: 109999099.99999961 reward: 252.49999999999915                       blocks_per_halving: 108910
# good max_supply found: 109999099.99999961 reward: 252.49999999999915                       blocks_per_halving: 108910
# good max_supply found: 209999199.99999937 reward: 252.49999999999915                       blocks_per_halving: 207920
# good max_supply found: 209999199.99999937 reward: 252.49999999999915                       blocks_per_halving: 207920
# good max_supply found: 209999199.99999937 reward: 252.49999999999915                       blocks_per_halving: 207920
# good max_supply found: 209999199.99999937 reward: 252.49999999999915                       blocks_per_halving: 207920
# good max_supply found: 309999299.9999989 reward: 252.49999999999915                       blocks_per_halving: 306930
# good max_supply found: 309999299.9999989 reward: 252.49999999999915                       blocks_per_halving: 306930
# good max_supply found: 309999299.9999989 reward: 252.49999999999915                       blocks_per_halving: 306930
# good max_supply found: 309999299.9999989 reward: 252.49999999999915                       blocks_per_halving: 306930
# good max_supply found: 409999399.9999986 reward: 252.49999999999915                       blocks_per_halving: 405940
# good max_supply found: 409999399.9999986 reward: 252.49999999999915                       blocks_per_halving: 405940
# good max_supply found: 409999399.9999986 reward: 252.49999999999915                       blocks_per_halving: 405940
# good max_supply found: 409999399.9999986 reward: 252.49999999999915                       blocks_per_halving: 405940
# good max_supply found: 509999499.9999986 reward: 252.49999999999915                       blocks_per_halving: 504950
# good max_supply found: 509999499.9999986 reward: 252.49999999999915                       blocks_per_halving: 504950
# good max_supply found: 509999499.9999986 reward: 252.49999999999915                       blocks_per_halving: 504950
# good max_supply found: 509999499.9999986 reward: 252.49999999999915                       blocks_per_halving: 504950
# good max_supply found: 209999361.59999916 reward: 254.51999999999913                       blocks_per_halving: 206270
# good max_supply found: 209999361.59999916 reward: 254.51999999999913                       blocks_per_halving: 206270
# good max_supply found: 209999361.59999916 reward: 254.51999999999913                       blocks_per_halving: 206270
# good max_supply found: 209999361.59999916 reward: 254.51999999999913                       blocks_per_halving: 206270
# good max_supply found: 309999259.59999883 reward: 259.5699999999991                       blocks_per_halving: 298570
# good max_supply found: 309999259.59999883 reward: 259.5699999999991                       blocks_per_halving: 298570
# good max_supply found: 309999259.59999883 reward: 259.5699999999991                       blocks_per_halving: 298570
# good max_supply found: 309999259.59999883 reward: 259.5699999999991                       blocks_per_halving: 298570
# good max_supply found: 609999882.7999977 reward: 259.5699999999991                       blocks_per_halving: 587510
# good max_supply found: 609999882.7999977 reward: 259.5699999999991                       blocks_per_halving: 587510
# good max_supply found: 609999882.7999977 reward: 259.5699999999991                       blocks_per_halving: 587510
# good max_supply found: 609999882.7999977 reward: 259.5699999999991                       blocks_per_halving: 587510
# good max_supply found: 109999180.79999958 reward: 263.60999999999905                       blocks_per_halving: 104320
# good max_supply found: 109999180.79999958 reward: 263.60999999999905                       blocks_per_halving: 104320
# good max_supply found: 109999180.79999958 reward: 263.60999999999905                       blocks_per_halving: 104320
# good max_supply found: 109999180.79999958 reward: 263.60999999999905                       blocks_per_halving: 104320
# good max_supply found: 509999903.99999833 reward: 269.669999999999                       blocks_per_halving: 472800
# good max_supply found: 509999903.99999833 reward: 269.669999999999                       blocks_per_halving: 472800
# good max_supply found: 509999903.99999833 reward: 269.669999999999                       blocks_per_halving: 472800
# good max_supply found: 509999903.99999833 reward: 269.669999999999                       blocks_per_halving: 472800
# good max_supply found: 609999276.7999971 reward: 274.71999999999895                       blocks_per_halving: 555110
# good max_supply found: 609999276.7999971 reward: 274.71999999999895                       blocks_per_halving: 555110
# good max_supply found: 609999276.7999971 reward: 274.71999999999895                       blocks_per_halving: 555110
# good max_supply found: 609999276.7999971 reward: 274.71999999999895                       blocks_per_halving: 555110
# good max_supply found: 409999480.7999984 reward: 275.72999999999894                       blocks_per_halving: 371740
# good max_supply found: 409999480.7999984 reward: 275.72999999999894                       blocks_per_halving: 371740
# good max_supply found: 409999480.7999984 reward: 275.72999999999894                       blocks_per_halving: 371740
# good max_supply found: 409999480.7999984 reward: 275.72999999999894                       blocks_per_halving: 371740
# good max_supply found: 609999317.1999974 reward: 279.7699999999989                       blocks_per_halving: 545090
# good max_supply found: 609999317.1999974 reward: 279.7699999999989                       blocks_per_halving: 545090
# good max_supply found: 609999317.1999974 reward: 279.7699999999989                       blocks_per_halving: 545090
# good max_supply found: 609999317.1999974 reward: 279.7699999999989                       blocks_per_halving: 545090
# good max_supply found: 109999544.39999944 reward: 281.7899999999989                       blocks_per_halving: 97590
# good max_supply found: 109999544.39999944 reward: 281.7899999999989                       blocks_per_halving: 97590
# good max_supply found: 109999544.39999944 reward: 281.7899999999989                       blocks_per_halving: 97590
# good max_supply found: 109999544.39999944 reward: 281.7899999999989                       blocks_per_halving: 97590
# good max_supply found: 609999599.9999976 reward: 282.7999999999989                       blocks_per_halving: 539250
# good max_supply found: 609999599.9999976 reward: 282.7999999999989                       blocks_per_halving: 539250
# good max_supply found: 609999599.9999976 reward: 282.7999999999989                       blocks_per_halving: 539250
# good max_supply found: 609999599.9999976 reward: 282.7999999999989                       blocks_per_halving: 539250
# good max_supply found: 309999986.7999984 reward: 283.80999999999887                       blocks_per_halving: 273070
# good max_supply found: 309999986.7999984 reward: 283.80999999999887                       blocks_per_halving: 273070
# good max_supply found: 309999986.7999984 reward: 283.80999999999887                       blocks_per_halving: 273070
# good max_supply found: 309999986.7999984 reward: 283.80999999999887                       blocks_per_halving: 273070
# good max_supply found: 309999784.7999984 reward: 285.82999999999885                       blocks_per_halving: 271140
# good max_supply found: 309999784.7999984 reward: 285.82999999999885                       blocks_per_halving: 271140
# good max_supply found: 309999784.7999984 reward: 285.82999999999885                       blocks_per_halving: 271140
# good max_supply found: 309999784.7999984 reward: 285.82999999999885                       blocks_per_halving: 271140
# good max_supply found: 509999661.59999806 reward: 288.8599999999988                       blocks_per_halving: 441390
# good max_supply found: 509999661.59999806 reward: 288.8599999999988                       blocks_per_halving: 441390
# good max_supply found: 509999661.59999806 reward: 288.8599999999988                       blocks_per_halving: 441390
# good max_supply found: 509999661.59999806 reward: 288.8599999999988                       blocks_per_halving: 441390
# good max_supply found: 109999867.59999953 reward: 289.8699999999988                       blocks_per_halving: 94870
# good max_supply found: 109999867.59999953 reward: 289.8699999999988                       blocks_per_halving: 94870
# good max_supply found: 109999867.59999953 reward: 289.8699999999988                       blocks_per_halving: 94870
# good max_supply found: 109999867.59999953 reward: 289.8699999999988                       blocks_per_halving: 94870
# good max_supply found: 109999180.7999995 reward: 290.8799999999988                       blocks_per_halving: 94540
# good max_supply found: 109999180.7999995 reward: 290.8799999999988                       blocks_per_halving: 94540
# good max_supply found: 109999180.7999995 reward: 290.8799999999988                       blocks_per_halving: 94540
# good max_supply found: 109999180.7999995 reward: 290.8799999999988                       blocks_per_halving: 94540
# good max_supply found: 509999257.5999978 reward: 294.91999999999877                       blocks_per_halving: 432320
# good max_supply found: 509999257.5999978 reward: 294.91999999999877                       blocks_per_halving: 432320
# good max_supply found: 509999257.5999978 reward: 294.91999999999877                       blocks_per_halving: 432320
# good max_supply found: 509999257.5999978 reward: 294.91999999999877                       blocks_per_halving: 432320
# good max_supply found: 309999097.99999875 reward: 297.94999999999874                       blocks_per_halving: 260110
# good max_supply found: 309999097.99999875 reward: 297.94999999999874                       blocks_per_halving: 260110
# good max_supply found: 309999097.99999875 reward: 297.94999999999874                       blocks_per_halving: 260110
# good max_supply found: 309999097.99999875 reward: 297.94999999999874                       blocks_per_halving: 260110
# good max_supply found: 209999765.59999907 reward: 300.9799999999987                       blocks_per_halving: 174430
# good max_supply found: 209999765.59999907 reward: 300.9799999999987                       blocks_per_halving: 174430
# good max_supply found: 209999765.59999907 reward: 300.9799999999987                       blocks_per_halving: 174430
# good max_supply found: 209999765.59999907 reward: 300.9799999999987                       blocks_per_halving: 174430
# good max_supply found: 709999780.7999967 reward: 300.9799999999987                       blocks_per_halving: 589740
# good max_supply found: 709999780.7999967 reward: 300.9799999999987                       blocks_per_halving: 589740
# good max_supply found: 709999780.7999967 reward: 300.9799999999987                       blocks_per_halving: 589740
# good max_supply found: 709999780.7999967 reward: 300.9799999999987                       blocks_per_halving: 589740
# good max_supply found: 609999599.9999974 reward: 302.9999999999987                       blocks_per_halving: 503300
# good max_supply found: 609999599.9999974 reward: 302.9999999999987                       blocks_per_halving: 503300
# good max_supply found: 609999599.9999974 reward: 302.9999999999987                       blocks_per_halving: 503300
# good max_supply found: 609999599.9999974 reward: 302.9999999999987                       blocks_per_halving: 503300
# good max_supply found: 109999423.19999951 reward: 306.02999999999867                       blocks_per_halving: 89860
# good max_supply found: 109999423.19999951 reward: 306.02999999999867                       blocks_per_halving: 89860
# good max_supply found: 109999423.19999951 reward: 306.02999999999867                       blocks_per_halving: 89860
# good max_supply found: 109999423.19999951 reward: 306.02999999999867                       blocks_per_halving: 89860
# good max_supply found: 309999865.5999986 reward: 307.03999999999866                       blocks_per_halving: 252410
# good max_supply found: 309999865.5999986 reward: 307.03999999999866                       blocks_per_halving: 252410
# good max_supply found: 309999865.5999986 reward: 307.03999999999866                       blocks_per_halving: 252410
# good max_supply found: 309999865.5999986 reward: 307.03999999999866                       blocks_per_halving: 252410
# good max_supply found: 709999295.9999968 reward: 307.03999999999866                       blocks_per_halving: 578100
# good max_supply found: 709999295.9999968 reward: 307.03999999999866                       blocks_per_halving: 578100
# good max_supply found: 709999295.9999968 reward: 307.03999999999866                       blocks_per_halving: 578100
# good max_supply found: 709999295.9999968 reward: 307.03999999999866                       blocks_per_halving: 578100
# good max_supply found: 309999542.39999866 reward: 309.05999999999864                       blocks_per_halving: 250760
# good max_supply found: 309999542.39999866 reward: 309.05999999999864                       blocks_per_halving: 250760
# good max_supply found: 309999542.39999866 reward: 309.05999999999864                       blocks_per_halving: 250760
# good max_supply found: 309999542.39999866 reward: 309.05999999999864                       blocks_per_halving: 250760
# good max_supply found: 409999359.59999824 reward: 310.06999999999863                       blocks_per_halving: 330570
# good max_supply found: 409999359.59999824 reward: 310.06999999999863                       blocks_per_halving: 330570
# good max_supply found: 409999359.59999824 reward: 310.06999999999863                       blocks_per_halving: 330570
# good max_supply found: 409999359.59999824 reward: 310.06999999999863                       blocks_per_halving: 330570
# good max_supply found: 209999119.19999912 reward: 312.0899999999986                       blocks_per_halving: 168220
# good max_supply found: 209999119.19999912 reward: 312.0899999999986                       blocks_per_halving: 168220
# good max_supply found: 209999119.19999912 reward: 312.0899999999986                       blocks_per_halving: 168220
# good max_supply found: 209999119.19999912 reward: 312.0899999999986                       blocks_per_halving: 168220
# good max_supply found: 509999176.7999976 reward: 317.13999999999857                       blocks_per_halving: 402030
# good max_supply found: 509999176.7999976 reward: 317.13999999999857                       blocks_per_halving: 402030
# good max_supply found: 509999176.7999976 reward: 317.13999999999857                       blocks_per_halving: 402030
# good max_supply found: 509999176.7999976 reward: 317.13999999999857                       blocks_per_halving: 402030
# good max_supply found: 609999761.5999967 reward: 317.13999999999857                       blocks_per_halving: 480860
# good max_supply found: 609999761.5999967 reward: 317.13999999999857                       blocks_per_halving: 480860
# good max_supply found: 609999761.5999967 reward: 317.13999999999857                       blocks_per_halving: 480860
# good max_supply found: 609999761.5999967 reward: 317.13999999999857                       blocks_per_halving: 480860
# good max_supply found: 309999703.99999857 reward: 325.2199999999985                       blocks_per_halving: 238300
# good max_supply found: 309999703.99999857 reward: 325.2199999999985                       blocks_per_halving: 238300
# good max_supply found: 309999703.99999857 reward: 325.2199999999985                       blocks_per_halving: 238300
# good max_supply found: 309999703.99999857 reward: 325.2199999999985                       blocks_per_halving: 238300
# good max_supply found: 309999299.99999845 reward: 328.24999999999847                       blocks_per_halving: 236100
# good max_supply found: 309999299.99999845 reward: 328.24999999999847                       blocks_per_halving: 236100
# good max_supply found: 309999299.99999845 reward: 328.24999999999847                       blocks_per_halving: 236100
# good max_supply found: 309999299.99999845 reward: 328.24999999999847                       blocks_per_halving: 236100
# good max_supply found: 109999180.79999948 reward: 329.25999999999846                       blocks_per_halving: 83520
# good max_supply found: 109999180.79999948 reward: 329.25999999999846                       blocks_per_halving: 83520
# good max_supply found: 109999180.79999948 reward: 329.25999999999846                       blocks_per_halving: 83520
# good max_supply found: 109999180.79999948 reward: 329.25999999999846                       blocks_per_halving: 83520
# good max_supply found: 709999295.9999967 reward: 331.27999999999844                       blocks_per_halving: 535800
# good max_supply found: 709999295.9999967 reward: 331.27999999999844                       blocks_per_halving: 535800
# good max_supply found: 709999295.9999967 reward: 331.27999999999844                       blocks_per_halving: 535800
# good max_supply found: 709999295.9999967 reward: 331.27999999999844                       blocks_per_halving: 535800
# good max_supply found: 309999986.7999982 reward: 332.28999999999843                       blocks_per_halving: 233230
# good max_supply found: 309999986.7999982 reward: 332.28999999999843                       blocks_per_halving: 233230
# good max_supply found: 309999986.7999982 reward: 332.28999999999843                       blocks_per_halving: 233230
# good max_supply found: 309999986.7999982 reward: 332.28999999999843                       blocks_per_halving: 233230
# good max_supply found: 409999723.1999981 reward: 336.3299999999984                       blocks_per_halving: 304760
# good max_supply found: 409999723.1999981 reward: 336.3299999999984                       blocks_per_halving: 304760
# good max_supply found: 409999723.1999981 reward: 336.3299999999984                       blocks_per_halving: 304760
# good max_supply found: 409999723.1999981 reward: 336.3299999999984                       blocks_per_halving: 304760
# good max_supply found: 109999827.19999942 reward: 337.3399999999984                       blocks_per_halving: 81520
# good max_supply found: 109999827.19999942 reward: 337.3399999999984                       blocks_per_halving: 81520
# good max_supply found: 109999827.19999942 reward: 337.3399999999984                       blocks_per_halving: 81520
# good max_supply found: 109999827.19999942 reward: 337.3399999999984                       blocks_per_halving: 81520
# good max_supply found: 809999153.5999956 reward: 341.37999999999835                       blocks_per_halving: 593180
# good max_supply found: 809999153.5999956 reward: 341.37999999999835                       blocks_per_halving: 593180
# good max_supply found: 809999153.5999956 reward: 341.37999999999835                       blocks_per_halving: 593180
# good max_supply found: 809999153.5999956 reward: 341.37999999999835                       blocks_per_halving: 593180
# good max_supply found: 309999905.99999833 reward: 342.38999999999834                       blocks_per_halving: 226350
# good max_supply found: 309999905.99999833 reward: 342.38999999999834                       blocks_per_halving: 226350
# good max_supply found: 309999905.99999833 reward: 342.38999999999834                       blocks_per_halving: 226350
# good max_supply found: 309999905.99999833 reward: 342.38999999999834                       blocks_per_halving: 226350
# good max_supply found: 409999440.399998 reward: 344.4099999999983                       blocks_per_halving: 297610
# good max_supply found: 409999440.399998 reward: 344.4099999999983                       blocks_per_halving: 297610
# good max_supply found: 409999440.399998 reward: 344.4099999999983                       blocks_per_halving: 297610
# good max_supply found: 409999440.399998 reward: 344.4099999999983                       blocks_per_halving: 297610
# good max_supply found: 10000131.199999996 reward: 8.08                       blocks_per_halving: 309410
# good max_supply found: 10000131.199999996 reward: 8.08                       blocks_per_halving: 309410
# good max_supply found: 10000131.199999996 reward: 8.08                       blocks_per_halving: 309410
# good max_supply found: 10000131.199999996 reward: 8.08                       blocks_per_halving: 309410
# good max_supply found: 10000454.399999993 reward: 8.08                       blocks_per_halving: 309420
# good max_supply found: 10000454.399999993 reward: 8.08                       blocks_per_halving: 309420
# good max_supply found: 10000454.399999993 reward: 8.08                       blocks_per_halving: 309420
# good max_supply found: 10000454.399999993 reward: 8.08                       blocks_per_halving: 309420
# good max_supply found: 10000454.399999993 reward: 16.16                       blocks_per_halving: 154710
# good max_supply found: 10000454.399999993 reward: 16.16                       blocks_per_halving: 154710
# good max_supply found: 10000454.399999993 reward: 16.16                       blocks_per_halving: 154710
# good max_supply found: 10000454.399999993 reward: 16.16                       blocks_per_halving: 154710
# good max_supply found: 20000262.39999999 reward: 16.16                       blocks_per_halving: 309410
# good max_supply found: 20000262.39999999 reward: 16.16                       blocks_per_halving: 309410
# good max_supply found: 20000262.39999999 reward: 16.16                       blocks_per_halving: 309410
# good max_supply found: 20000262.39999999 reward: 16.16                       blocks_per_halving: 309410
# good max_supply found: 30000070.399999995 reward: 16.16                       blocks_per_halving: 464110
# good max_supply found: 30000070.399999995 reward: 16.16                       blocks_per_halving: 464110
# good max_supply found: 30000070.399999995 reward: 16.16                       blocks_per_halving: 464110
# good max_supply found: 30000070.399999995 reward: 16.16                       blocks_per_halving: 464110
# good max_supply found: 50000332.80000003 reward: 32.32                       blocks_per_halving: 386760
# good max_supply found: 50000332.80000003 reward: 32.32                       blocks_per_halving: 386760
# good max_supply found: 50000332.80000003 reward: 32.32                       blocks_per_halving: 386760
# good max_supply found: 50000332.80000003 reward: 32.32                       blocks_per_halving: 386760
# good max_supply found: 60000140.79999999 reward: 32.32                       blocks_per_halving: 464110
# good max_supply found: 60000140.79999999 reward: 32.32                       blocks_per_halving: 464110
# good max_supply found: 60000140.79999999 reward: 32.32                       blocks_per_halving: 464110
# good max_supply found: 60000140.79999999 reward: 32.32                       blocks_per_halving: 464110
# good max_supply found: 50000332.80000003 reward: 64.64                       blocks_per_halving: 193380
# good max_supply found: 50000332.80000003 reward: 64.64                       blocks_per_halving: 193380
# good max_supply found: 50000332.80000003 reward: 64.64                       blocks_per_halving: 193380
# good max_supply found: 50000332.80000003 reward: 64.64                       blocks_per_halving: 193380
# good max_supply found: 50000332.80000003 reward: 129.28                       blocks_per_halving: 96690
# good max_supply found: 50000332.80000003 reward: 129.28                       blocks_per_halving: 96690
# good max_supply found: 50000332.80000003 reward: 129.28                       blocks_per_halving: 96690
# good max_supply found: 50000332.80000003 reward: 129.28                       blocks_per_halving: 96690
# good max_supply found: 1029999615.9999996 reward: 517.12                       blocks_per_halving: 497950
# good max_supply found: 1029999615.9999996 reward: 517.12                       blocks_per_halving: 497950
# good max_supply found: 1029999615.9999996 reward: 517.12                       blocks_per_halving: 497950
# good max_supply found: 1029999615.9999996 reward: 517.12                       blocks_per_halving: 497950
# good max_supply found: 10004009.599999994 reward: 8.08                       blocks_per_halving: 309530
# good max_supply found: 10004009.599999994 reward: 8.08                       blocks_per_halving: 309530
# good max_supply found: 10004009.599999994 reward: 8.08                       blocks_per_halving: 309530
# good max_supply found: 10004009.599999994 reward: 8.08                       blocks_per_halving: 309530
# good max_supply found: 10004332.799999991 reward: 8.08                       blocks_per_halving: 309540
# good max_supply found: 10004332.799999991 reward: 8.08                       blocks_per_halving: 309540
# good max_supply found: 10004332.799999991 reward: 8.08                       blocks_per_halving: 309540
# good max_supply found: 10004332.799999991 reward: 8.08                       blocks_per_halving: 309540
# good max_supply found: 10004656.0 reward: 8.08                       blocks_per_halving: 309550
# good max_supply found: 10004656.0 reward: 8.08                       blocks_per_halving: 309550
# good max_supply found: 10004656.0 reward: 8.08                       blocks_per_halving: 309550
# good max_supply found: 10004656.0 reward: 8.08                       blocks_per_halving: 309550
# good max_supply found: 10004979.199999994 reward: 8.08                       blocks_per_halving: 309560
# good max_supply found: 10004979.199999994 reward: 8.08                       blocks_per_halving: 309560
# good max_supply found: 10004979.199999994 reward: 8.08                       blocks_per_halving: 309560
# good max_supply found: 10004979.199999994 reward: 8.08                       blocks_per_halving: 309560
# good max_supply found: 10000454.399999993 reward: 16.16                       blocks_per_halving: 154710
# good max_supply found: 10000454.399999993 reward: 16.16                       blocks_per_halving: 154710
# good max_supply found: 10000454.399999993 reward: 16.16                       blocks_per_halving: 154710
# good max_supply found: 10000454.399999993 reward: 16.16                       blocks_per_halving: 154710
# good max_supply found: 10001100.799999997 reward: 16.16                       blocks_per_halving: 154720
# good max_supply found: 10001100.799999997 reward: 16.16                       blocks_per_halving: 154720
# good max_supply found: 10001100.799999997 reward: 16.16                       blocks_per_halving: 154720
# good max_supply found: 10001100.799999997 reward: 16.16                       blocks_per_halving: 154720
# good max_supply found: 10001747.200000003 reward: 16.16                       blocks_per_halving: 154730
# good max_supply found: 10001747.200000003 reward: 16.16                       blocks_per_halving: 154730
# good max_supply found: 10001747.200000003 reward: 16.16                       blocks_per_halving: 154730
# good max_supply found: 10001747.200000003 reward: 16.16                       blocks_per_halving: 154730
# good max_supply found: 10002393.599999996 reward: 16.16                       blocks_per_halving: 154740
# good max_supply found: 10002393.599999996 reward: 16.16                       blocks_per_halving: 154740
# good max_supply found: 10002393.599999996 reward: 16.16                       blocks_per_halving: 154740
# good max_supply found: 10002393.599999996 reward: 16.16                       blocks_per_halving: 154740
# good max_supply found: 10003040.000000004 reward: 16.16                       blocks_per_halving: 154750
# good max_supply found: 10003040.000000004 reward: 16.16                       blocks_per_halving: 154750
# good max_supply found: 10003040.000000004 reward: 16.16                       blocks_per_halving: 154750
# good max_supply found: 10003040.000000004 reward: 16.16                       blocks_per_halving: 154750
# good max_supply found: 10003686.399999997 reward: 16.16                       blocks_per_halving: 154760
# good max_supply found: 10003686.399999997 reward: 16.16                       blocks_per_halving: 154760
# good max_supply found: 10003686.399999997 reward: 16.16                       blocks_per_halving: 154760
# good max_supply found: 10003686.399999997 reward: 16.16                       blocks_per_halving: 154760
# good max_supply found: 10004332.799999991 reward: 16.16                       blocks_per_halving: 154770
# good max_supply found: 10004332.799999991 reward: 16.16                       blocks_per_halving: 154770
# good max_supply found: 10004332.799999991 reward: 16.16                       blocks_per_halving: 154770
# good max_supply found: 10004332.799999991 reward: 16.16                       blocks_per_halving: 154770
# good max_supply found: 10004979.199999994 reward: 16.16                       blocks_per_halving: 154780
# good max_supply found: 10004979.199999994 reward: 16.16                       blocks_per_halving: 154780
# good max_supply found: 10004979.199999994 reward: 16.16                       blocks_per_halving: 154780
# good max_supply found: 10004979.199999994 reward: 16.16                       blocks_per_halving: 154780
# good max_supply found: 20000262.39999999 reward: 16.16                       blocks_per_halving: 309410
# good max_supply found: 20000262.39999999 reward: 16.16                       blocks_per_halving: 309410
# good max_supply found: 20000262.39999999 reward: 16.16                       blocks_per_halving: 309410
# good max_supply found: 20000262.39999999 reward: 16.16                       blocks_per_halving: 309410
# good max_supply found: 20000908.799999986 reward: 16.16                       blocks_per_halving: 309420
# good max_supply found: 20000908.799999986 reward: 16.16                       blocks_per_halving: 309420
# good max_supply found: 20000908.799999986 reward: 16.16                       blocks_per_halving: 309420
# good max_supply found: 20000908.799999986 reward: 16.16                       blocks_per_halving: 309420
# good max_supply found: 20001555.2 reward: 16.16                       blocks_per_halving: 309430
# good max_supply found: 20001555.2 reward: 16.16                       blocks_per_halving: 309430
# good max_supply found: 20001555.2 reward: 16.16                       blocks_per_halving: 309430
# good max_supply found: 20001555.2 reward: 16.16                       blocks_per_halving: 309430
# good max_supply found: 20002201.599999994 reward: 16.16                       blocks_per_halving: 309440
# good max_supply found: 20002201.599999994 reward: 16.16                       blocks_per_halving: 309440
# good max_supply found: 20002201.599999994 reward: 16.16                       blocks_per_halving: 309440
# good max_supply found: 20002201.599999994 reward: 16.16                       blocks_per_halving: 309440
# good max_supply found: 20002847.99999997 reward: 16.16                       blocks_per_halving: 309450
# good max_supply found: 20002847.99999997 reward: 16.16                       blocks_per_halving: 309450
# good max_supply found: 20002847.99999997 reward: 16.16                       blocks_per_halving: 309450
# good max_supply found: 20002847.99999997 reward: 16.16                       blocks_per_halving: 309450
# good max_supply found: 20003494.400000006 reward: 16.16                       blocks_per_halving: 309460
# good max_supply found: 20003494.400000006 reward: 16.16                       blocks_per_halving: 309460
# good max_supply found: 20003494.400000006 reward: 16.16                       blocks_per_halving: 309460
# good max_supply found: 20003494.400000006 reward: 16.16                       blocks_per_halving: 309460
# good max_supply found: 20004140.80000001 reward: 16.16                       blocks_per_halving: 309470
# good max_supply found: 20004140.80000001 reward: 16.16                       blocks_per_halving: 309470
# good max_supply found: 20004140.80000001 reward: 16.16                       blocks_per_halving: 309470
# good max_supply found: 20004140.80000001 reward: 16.16                       blocks_per_halving: 309470
# good max_supply found: 20004787.19999999 reward: 16.16                       blocks_per_halving: 309480
# good max_supply found: 20004787.19999999 reward: 16.16                       blocks_per_halving: 309480
# good max_supply found: 20004787.19999999 reward: 16.16                       blocks_per_halving: 309480
# good max_supply found: 20004787.19999999 reward: 16.16                       blocks_per_halving: 309480
# good max_supply found: 30000070.399999995 reward: 16.16                       blocks_per_halving: 464110
# good max_supply found: 30000070.399999995 reward: 16.16                       blocks_per_halving: 464110
# good max_supply found: 30000070.399999995 reward: 16.16                       blocks_per_halving: 464110
# good max_supply found: 30000070.399999995 reward: 16.16                       blocks_per_halving: 464110
# good max_supply found: 30000716.799999993 reward: 16.16                       blocks_per_halving: 464120
# good max_supply found: 30000716.799999993 reward: 16.16                       blocks_per_halving: 464120
# good max_supply found: 30000716.799999993 reward: 16.16                       blocks_per_halving: 464120
# good max_supply found: 30000716.799999993 reward: 16.16                       blocks_per_halving: 464120
# good max_supply found: 30001363.199999988 reward: 16.16                       blocks_per_halving: 464130
# good max_supply found: 30001363.199999988 reward: 16.16                       blocks_per_halving: 464130
# good max_supply found: 30001363.199999988 reward: 16.16                       blocks_per_halving: 464130
# good max_supply found: 30001363.199999988 reward: 16.16                       blocks_per_halving: 464130
# good max_supply found: 30002009.59999999 reward: 16.16                       blocks_per_halving: 464140
# good max_supply found: 30002009.59999999 reward: 16.16                       blocks_per_halving: 464140
# good max_supply found: 30002009.59999999 reward: 16.16                       blocks_per_halving: 464140
# good max_supply found: 30002009.59999999 reward: 16.16                       blocks_per_halving: 464140
# good max_supply found: 30002655.999999985 reward: 16.16                       blocks_per_halving: 464150
# good max_supply found: 30002655.999999985 reward: 16.16                       blocks_per_halving: 464150
# good max_supply found: 30002655.999999985 reward: 16.16                       blocks_per_halving: 464150
# good max_supply found: 30002655.999999985 reward: 16.16                       blocks_per_halving: 464150
# good max_supply found: 30003302.39999999 reward: 16.16                       blocks_per_halving: 464160
# good max_supply found: 30003302.39999999 reward: 16.16                       blocks_per_halving: 464160
# good max_supply found: 30003302.39999999 reward: 16.16                       blocks_per_halving: 464160
# good max_supply found: 30003302.39999999 reward: 16.16                       blocks_per_halving: 464160
# good max_supply found: 30003948.799999997 reward: 16.16                       blocks_per_halving: 464170
# good max_supply found: 30003948.799999997 reward: 16.16                       blocks_per_halving: 464170
# good max_supply found: 30003948.799999997 reward: 16.16                       blocks_per_halving: 464170
# good max_supply found: 30003948.799999997 reward: 16.16                       blocks_per_halving: 464170
# good max_supply found: 30004595.199999977 reward: 16.16                       blocks_per_halving: 464180
# good max_supply found: 30004595.199999977 reward: 16.16                       blocks_per_halving: 464180
# good max_supply found: 30004595.199999977 reward: 16.16                       blocks_per_halving: 464180
# good max_supply found: 30004595.199999977 reward: 16.16                       blocks_per_halving: 464180
# good max_supply found: 10001100.799999997 reward: 32.32                       blocks_per_halving: 77360
# good max_supply found: 10001100.799999997 reward: 32.32                       blocks_per_halving: 77360
# good max_supply found: 10001100.799999997 reward: 32.32                       blocks_per_halving: 77360
# good max_supply found: 10001100.799999997 reward: 32.32                       blocks_per_halving: 77360
# good max_supply found: 10002393.599999996 reward: 32.32                       blocks_per_halving: 77370
# good max_supply found: 10002393.599999996 reward: 32.32                       blocks_per_halving: 77370
# good max_supply found: 10002393.599999996 reward: 32.32                       blocks_per_halving: 77370
# good max_supply found: 10002393.599999996 reward: 32.32                       blocks_per_halving: 77370
# good max_supply found: 10003686.399999997 reward: 32.32                       blocks_per_halving: 77380
# good max_supply found: 10003686.399999997 reward: 32.32                       blocks_per_halving: 77380
# good max_supply found: 10003686.399999997 reward: 32.32                       blocks_per_halving: 77380
# good max_supply found: 10003686.399999997 reward: 32.32                       blocks_per_halving: 77380
# good max_supply found: 10004979.199999994 reward: 32.32                       blocks_per_halving: 77390
# good max_supply found: 10004979.199999994 reward: 32.32                       blocks_per_halving: 77390
# good max_supply found: 10004979.199999994 reward: 32.32                       blocks_per_halving: 77390
# good max_supply found: 10004979.199999994 reward: 32.32                       blocks_per_halving: 77390
# good max_supply found: 20000908.799999986 reward: 32.32                       blocks_per_halving: 154710
# good max_supply found: 20000908.799999986 reward: 32.32                       blocks_per_halving: 154710
# good max_supply found: 20000908.799999986 reward: 32.32                       blocks_per_halving: 154710
# good max_supply found: 20000908.799999986 reward: 32.32                       blocks_per_halving: 154710
# good max_supply found: 20002201.599999994 reward: 32.32                       blocks_per_halving: 154720
# good max_supply found: 20002201.599999994 reward: 32.32                       blocks_per_halving: 154720
# good max_supply found: 20002201.599999994 reward: 32.32                       blocks_per_halving: 154720
# good max_supply found: 20002201.599999994 reward: 32.32                       blocks_per_halving: 154720
# good max_supply found: 20003494.400000006 reward: 32.32                       blocks_per_halving: 154730
# good max_supply found: 20003494.400000006 reward: 32.32                       blocks_per_halving: 154730
# good max_supply found: 20003494.400000006 reward: 32.32                       blocks_per_halving: 154730
# good max_supply found: 20003494.400000006 reward: 32.32                       blocks_per_halving: 154730
# good max_supply found: 20004787.19999999 reward: 32.32                       blocks_per_halving: 154740
# good max_supply found: 20004787.19999999 reward: 32.32                       blocks_per_halving: 154740
# good max_supply found: 20004787.19999999 reward: 32.32                       blocks_per_halving: 154740
# good max_supply found: 20004787.19999999 reward: 32.32                       blocks_per_halving: 154740
# good max_supply found: 30000716.799999993 reward: 32.32                       blocks_per_halving: 232060
# good max_supply found: 30000716.799999993 reward: 32.32                       blocks_per_halving: 232060
# good max_supply found: 30000716.799999993 reward: 32.32                       blocks_per_halving: 232060
# good max_supply found: 30000716.799999993 reward: 32.32                       blocks_per_halving: 232060
# good max_supply found: 30002009.59999999 reward: 32.32                       blocks_per_halving: 232070
# good max_supply found: 30002009.59999999 reward: 32.32                       blocks_per_halving: 232070
# good max_supply found: 30002009.59999999 reward: 32.32                       blocks_per_halving: 232070
# good max_supply found: 30002009.59999999 reward: 32.32                       blocks_per_halving: 232070
# good max_supply found: 30003302.39999999 reward: 32.32                       blocks_per_halving: 232080
# good max_supply found: 30003302.39999999 reward: 32.32                       blocks_per_halving: 232080
# good max_supply found: 30003302.39999999 reward: 32.32                       blocks_per_halving: 232080
# good max_supply found: 30003302.39999999 reward: 32.32                       blocks_per_halving: 232080
# good max_supply found: 30004595.199999977 reward: 32.32                       blocks_per_halving: 232090
# good max_supply found: 30004595.199999977 reward: 32.32                       blocks_per_halving: 232090
# good max_supply found: 30004595.199999977 reward: 32.32                       blocks_per_halving: 232090
# good max_supply found: 30004595.199999977 reward: 32.32                       blocks_per_halving: 232090
# good max_supply found: 40000524.79999998 reward: 32.32                       blocks_per_halving: 309410
# good max_supply found: 40000524.79999998 reward: 32.32                       blocks_per_halving: 309410
# good max_supply found: 40000524.79999998 reward: 32.32                       blocks_per_halving: 309410
# good max_supply found: 40000524.79999998 reward: 32.32                       blocks_per_halving: 309410
# good max_supply found: 40001817.59999997 reward: 32.32                       blocks_per_halving: 309420
# good max_supply found: 40001817.59999997 reward: 32.32                       blocks_per_halving: 309420
# good max_supply found: 40001817.59999997 reward: 32.32                       blocks_per_halving: 309420
# good max_supply found: 40001817.59999997 reward: 32.32                       blocks_per_halving: 309420
# good max_supply found: 40003110.4 reward: 32.32                       blocks_per_halving: 309430
# good max_supply found: 40003110.4 reward: 32.32                       blocks_per_halving: 309430
# good max_supply found: 40003110.4 reward: 32.32                       blocks_per_halving: 309430
# good max_supply found: 40003110.4 reward: 32.32                       blocks_per_halving: 309430
# good max_supply found: 40004403.19999999 reward: 32.32                       blocks_per_halving: 309440
# good max_supply found: 40004403.19999999 reward: 32.32                       blocks_per_halving: 309440
# good max_supply found: 40004403.19999999 reward: 32.32                       blocks_per_halving: 309440
# good max_supply found: 40004403.19999999 reward: 32.32                       blocks_per_halving: 309440
# good max_supply found: 50000332.80000003 reward: 32.32                       blocks_per_halving: 386760
# good max_supply found: 50000332.80000003 reward: 32.32                       blocks_per_halving: 386760
# good max_supply found: 50000332.80000003 reward: 32.32                       blocks_per_halving: 386760
# good max_supply found: 50000332.80000003 reward: 32.32                       blocks_per_halving: 386760
# good max_supply found: 50001625.59999998 reward: 32.32                       blocks_per_halving: 386770
# good max_supply found: 50001625.59999998 reward: 32.32                       blocks_per_halving: 386770
# good max_supply found: 50001625.59999998 reward: 32.32                       blocks_per_halving: 386770
# good max_supply found: 50001625.59999998 reward: 32.32                       blocks_per_halving: 386770
# good max_supply found: 50002918.40000003 reward: 32.32                       blocks_per_halving: 386780
# good max_supply found: 50002918.40000003 reward: 32.32                       blocks_per_halving: 386780
# good max_supply found: 50002918.40000003 reward: 32.32                       blocks_per_halving: 386780
# good max_supply found: 50002918.40000003 reward: 32.32                       blocks_per_halving: 386780
# good max_supply found: 50004211.199999996 reward: 32.32                       blocks_per_halving: 386790
# good max_supply found: 50004211.199999996 reward: 32.32                       blocks_per_halving: 386790
# good max_supply found: 50004211.199999996 reward: 32.32                       blocks_per_halving: 386790
# good max_supply found: 50004211.199999996 reward: 32.32                       blocks_per_halving: 386790
# good max_supply found: 60000140.79999999 reward: 32.32                       blocks_per_halving: 464110
# good max_supply found: 60000140.79999999 reward: 32.32                       blocks_per_halving: 464110
# good max_supply found: 60000140.79999999 reward: 32.32                       blocks_per_halving: 464110
# good max_supply found: 60000140.79999999 reward: 32.32                       blocks_per_halving: 464110
# good max_supply found: 60001433.59999999 reward: 32.32                       blocks_per_halving: 464120
# good max_supply found: 60001433.59999999 reward: 32.32                       blocks_per_halving: 464120
# good max_supply found: 60001433.59999999 reward: 32.32                       blocks_per_halving: 464120
# good max_supply found: 60001433.59999999 reward: 32.32                       blocks_per_halving: 464120
# good max_supply found: 60002726.399999976 reward: 32.32                       blocks_per_halving: 464130
# good max_supply found: 60002726.399999976 reward: 32.32                       blocks_per_halving: 464130
# good max_supply found: 60002726.399999976 reward: 32.32                       blocks_per_halving: 464130
# good max_supply found: 60002726.399999976 reward: 32.32                       blocks_per_halving: 464130
# good max_supply found: 60004019.19999998 reward: 32.32                       blocks_per_halving: 464140
# good max_supply found: 60004019.19999998 reward: 32.32                       blocks_per_halving: 464140
# good max_supply found: 60004019.19999998 reward: 32.32                       blocks_per_halving: 464140
# good max_supply found: 60004019.19999998 reward: 32.32                       blocks_per_halving: 464140
# good max_supply found: 70001241.6 reward: 32.32                       blocks_per_halving: 541470
# good max_supply found: 70001241.6 reward: 32.32                       blocks_per_halving: 541470
# good max_supply found: 70001241.6 reward: 32.32                       blocks_per_halving: 541470
# good max_supply found: 70001241.6 reward: 32.32                       blocks_per_halving: 541470
# good max_supply found: 70002534.39999998 reward: 32.32                       blocks_per_halving: 541480
# good max_supply found: 70002534.39999998 reward: 32.32                       blocks_per_halving: 541480
# good max_supply found: 70002534.39999998 reward: 32.32                       blocks_per_halving: 541480
# good max_supply found: 70002534.39999998 reward: 32.32                       blocks_per_halving: 541480
# good max_supply found: 70003827.20000002 reward: 32.32                       blocks_per_halving: 541490
# good max_supply found: 70003827.20000002 reward: 32.32                       blocks_per_halving: 541490
# good max_supply found: 70003827.20000002 reward: 32.32                       blocks_per_halving: 541490
# good max_supply found: 70003827.20000002 reward: 32.32                       blocks_per_halving: 541490
# good max_supply found: 10001100.799999997 reward: 64.64                       blocks_per_halving: 38680
# good max_supply found: 10001100.799999997 reward: 64.64                       blocks_per_halving: 38680
# good max_supply found: 10001100.799999997 reward: 64.64                       blocks_per_halving: 38680
# good max_supply found: 10001100.799999997 reward: 64.64                       blocks_per_halving: 38680
# good max_supply found: 10003686.399999997 reward: 64.64                       blocks_per_halving: 38690
# good max_supply found: 10003686.399999997 reward: 64.64                       blocks_per_halving: 38690
# good max_supply found: 10003686.399999997 reward: 64.64                       blocks_per_halving: 38690
# good max_supply found: 10003686.399999997 reward: 64.64                       blocks_per_halving: 38690
# good max_supply found: 20002201.599999994 reward: 64.64                       blocks_per_halving: 77360
# good max_supply found: 20002201.599999994 reward: 64.64                       blocks_per_halving: 77360
# good max_supply found: 20002201.599999994 reward: 64.64                       blocks_per_halving: 77360
# good max_supply found: 20002201.599999994 reward: 64.64                       blocks_per_halving: 77360
# good max_supply found: 20004787.19999999 reward: 64.64                       blocks_per_halving: 77370
# good max_supply found: 20004787.19999999 reward: 64.64                       blocks_per_halving: 77370
# good max_supply found: 20004787.19999999 reward: 64.64                       blocks_per_halving: 77370
# good max_supply found: 20004787.19999999 reward: 64.64                       blocks_per_halving: 77370
# good max_supply found: 30000716.799999993 reward: 64.64                       blocks_per_halving: 116030
# good max_supply found: 30000716.799999993 reward: 64.64                       blocks_per_halving: 116030
# good max_supply found: 30000716.799999993 reward: 64.64                       blocks_per_halving: 116030
# good max_supply found: 30000716.799999993 reward: 64.64                       blocks_per_halving: 116030
# good max_supply found: 30003302.39999999 reward: 64.64                       blocks_per_halving: 116040
# good max_supply found: 30003302.39999999 reward: 64.64                       blocks_per_halving: 116040
# good max_supply found: 30003302.39999999 reward: 64.64                       blocks_per_halving: 116040
# good max_supply found: 30003302.39999999 reward: 64.64                       blocks_per_halving: 116040
# good max_supply found: 40001817.59999997 reward: 64.64                       blocks_per_halving: 154710
# good max_supply found: 40001817.59999997 reward: 64.64                       blocks_per_halving: 154710
# good max_supply found: 40001817.59999997 reward: 64.64                       blocks_per_halving: 154710
# good max_supply found: 40001817.59999997 reward: 64.64                       blocks_per_halving: 154710
# good max_supply found: 40004403.19999999 reward: 64.64                       blocks_per_halving: 154720
# good max_supply found: 40004403.19999999 reward: 64.64                       blocks_per_halving: 154720
# good max_supply found: 40004403.19999999 reward: 64.64                       blocks_per_halving: 154720
# good max_supply found: 40004403.19999999 reward: 64.64                       blocks_per_halving: 154720
# good max_supply found: 50000332.80000003 reward: 64.64                       blocks_per_halving: 193380
# good max_supply found: 50000332.80000003 reward: 64.64                       blocks_per_halving: 193380
# good max_supply found: 50000332.80000003 reward: 64.64                       blocks_per_halving: 193380
# good max_supply found: 50000332.80000003 reward: 64.64                       blocks_per_halving: 193380
# good max_supply found: 50002918.40000003 reward: 64.64                       blocks_per_halving: 193390
# good max_supply found: 50002918.40000003 reward: 64.64                       blocks_per_halving: 193390
# good max_supply found: 50002918.40000003 reward: 64.64                       blocks_per_halving: 193390
# good max_supply found: 50002918.40000003 reward: 64.64                       blocks_per_halving: 193390
# good max_supply found: 60001433.59999999 reward: 64.64                       blocks_per_halving: 232060
# good max_supply found: 60001433.59999999 reward: 64.64                       blocks_per_halving: 232060
# good max_supply found: 60001433.59999999 reward: 64.64                       blocks_per_halving: 232060
# good max_supply found: 60001433.59999999 reward: 64.64                       blocks_per_halving: 232060
# good max_supply found: 60004019.19999998 reward: 64.64                       blocks_per_halving: 232070
# good max_supply found: 60004019.19999998 reward: 64.64                       blocks_per_halving: 232070
# good max_supply found: 60004019.19999998 reward: 64.64                       blocks_per_halving: 232070
# good max_supply found: 60004019.19999998 reward: 64.64                       blocks_per_halving: 232070
# good max_supply found: 70002534.39999998 reward: 64.64                       blocks_per_halving: 270740
# good max_supply found: 70002534.39999998 reward: 64.64                       blocks_per_halving: 270740
# good max_supply found: 70002534.39999998 reward: 64.64                       blocks_per_halving: 270740
# good max_supply found: 70002534.39999998 reward: 64.64                       blocks_per_halving: 270740
# good max_supply found: 80001049.59999996 reward: 64.64                       blocks_per_halving: 309410
# good max_supply found: 80001049.59999996 reward: 64.64                       blocks_per_halving: 309410
# good max_supply found: 80001049.59999996 reward: 64.64                       blocks_per_halving: 309410
# good max_supply found: 80001049.59999996 reward: 64.64                       blocks_per_halving: 309410
# good max_supply found: 80003635.19999994 reward: 64.64                       blocks_per_halving: 309420
# good max_supply found: 80003635.19999994 reward: 64.64                       blocks_per_halving: 309420
# good max_supply found: 80003635.19999994 reward: 64.64                       blocks_per_halving: 309420
# good max_supply found: 80003635.19999994 reward: 64.64                       blocks_per_halving: 309420
# good max_supply found: 90002150.39999996 reward: 64.64                       blocks_per_halving: 348090
# good max_supply found: 90002150.39999996 reward: 64.64                       blocks_per_halving: 348090
# good max_supply found: 90002150.39999996 reward: 64.64                       blocks_per_halving: 348090
# good max_supply found: 90002150.39999996 reward: 64.64                       blocks_per_halving: 348090
# good max_supply found: 90004735.99999996 reward: 64.64                       blocks_per_halving: 348100
# good max_supply found: 90004735.99999996 reward: 64.64                       blocks_per_halving: 348100
# good max_supply found: 90004735.99999996 reward: 64.64                       blocks_per_halving: 348100
# good max_supply found: 90004735.99999996 reward: 64.64                       blocks_per_halving: 348100
# good max_supply found: 100000665.60000005 reward: 64.64                       blocks_per_halving: 386760
# good max_supply found: 100000665.60000005 reward: 64.64                       blocks_per_halving: 386760
# good max_supply found: 100000665.60000005 reward: 64.64                       blocks_per_halving: 386760
# good max_supply found: 100000665.60000005 reward: 64.64                       blocks_per_halving: 386760
# good max_supply found: 100003251.19999996 reward: 64.64                       blocks_per_halving: 386770
# good max_supply found: 100003251.19999996 reward: 64.64                       blocks_per_halving: 386770
# good max_supply found: 100003251.19999996 reward: 64.64                       blocks_per_halving: 386770
# good max_supply found: 100003251.19999996 reward: 64.64                       blocks_per_halving: 386770
# good max_supply found: 109996595.20000003 reward: 64.64                       blocks_per_halving: 425420
# good max_supply found: 109996595.20000003 reward: 64.64                       blocks_per_halving: 425420
# good max_supply found: 109996595.20000003 reward: 64.64                       blocks_per_halving: 425420
# good max_supply found: 109996595.20000003 reward: 64.64                       blocks_per_halving: 425420
# good max_supply found: 109999180.79999997 reward: 64.64                       blocks_per_halving: 425430
# good max_supply found: 109999180.79999997 reward: 64.64                       blocks_per_halving: 425430
# good max_supply found: 109999180.79999997 reward: 64.64                       blocks_per_halving: 425430
# good max_supply found: 109999180.79999997 reward: 64.64                       blocks_per_halving: 425430
# good max_supply found: 10001100.799999997 reward: 129.28                       blocks_per_halving: 19340
# good max_supply found: 10001100.799999997 reward: 129.28                       blocks_per_halving: 19340
# good max_supply found: 10001100.799999997 reward: 129.28                       blocks_per_halving: 19340
# good max_supply found: 10001100.799999997 reward: 129.28                       blocks_per_halving: 19340
# good max_supply found: 20002201.599999994 reward: 129.28                       blocks_per_halving: 38680
# good max_supply found: 20002201.599999994 reward: 129.28                       blocks_per_halving: 38680
# good max_supply found: 20002201.599999994 reward: 129.28                       blocks_per_halving: 38680
# good max_supply found: 20002201.599999994 reward: 129.28                       blocks_per_halving: 38680
# good max_supply found: 30003302.39999999 reward: 129.28                       blocks_per_halving: 58020
# good max_supply found: 30003302.39999999 reward: 129.28                       blocks_per_halving: 58020
# good max_supply found: 30003302.39999999 reward: 129.28                       blocks_per_halving: 58020
# good max_supply found: 30003302.39999999 reward: 129.28                       blocks_per_halving: 58020
# good max_supply found: 40004403.19999999 reward: 129.28                       blocks_per_halving: 77360
# good max_supply found: 40004403.19999999 reward: 129.28                       blocks_per_halving: 77360
# good max_supply found: 40004403.19999999 reward: 129.28                       blocks_per_halving: 77360
# good max_supply found: 40004403.19999999 reward: 129.28                       blocks_per_halving: 77360
# good max_supply found: 50000332.80000003 reward: 129.28                       blocks_per_halving: 96690
# good max_supply found: 50000332.80000003 reward: 129.28                       blocks_per_halving: 96690
# good max_supply found: 50000332.80000003 reward: 129.28                       blocks_per_halving: 96690
# good max_supply found: 50000332.80000003 reward: 129.28                       blocks_per_halving: 96690
# good max_supply found: 60001433.59999999 reward: 129.28                       blocks_per_halving: 116030
# good max_supply found: 60001433.59999999 reward: 129.28                       blocks_per_halving: 116030
# good max_supply found: 60001433.59999999 reward: 129.28                       blocks_per_halving: 116030
# good max_supply found: 60001433.59999999 reward: 129.28                       blocks_per_halving: 116030
# good max_supply found: 70002534.39999998 reward: 129.28                       blocks_per_halving: 135370
# good max_supply found: 70002534.39999998 reward: 129.28                       blocks_per_halving: 135370
# good max_supply found: 70002534.39999998 reward: 129.28                       blocks_per_halving: 135370
# good max_supply found: 70002534.39999998 reward: 129.28                       blocks_per_halving: 135370
# good max_supply found: 80003635.19999994 reward: 129.28                       blocks_per_halving: 154710
# good max_supply found: 80003635.19999994 reward: 129.28                       blocks_per_halving: 154710
# good max_supply found: 80003635.19999994 reward: 129.28                       blocks_per_halving: 154710
# good max_supply found: 80003635.19999994 reward: 129.28                       blocks_per_halving: 154710
# good max_supply found: 90004735.99999996 reward: 129.28                       blocks_per_halving: 174050
# good max_supply found: 90004735.99999996 reward: 129.28                       blocks_per_halving: 174050
# good max_supply found: 90004735.99999996 reward: 129.28                       blocks_per_halving: 174050
# good max_supply found: 90004735.99999996 reward: 129.28                       blocks_per_halving: 174050
# good max_supply found: 100000665.60000005 reward: 129.28                       blocks_per_halving: 193380
# good max_supply found: 100000665.60000005 reward: 129.28                       blocks_per_halving: 193380
# good max_supply found: 100000665.60000005 reward: 129.28                       blocks_per_halving: 193380
# good max_supply found: 100000665.60000005 reward: 129.28                       blocks_per_halving: 193380
# good max_supply found: 109996595.20000003 reward: 129.28                       blocks_per_halving: 212710
# good max_supply found: 109996595.20000003 reward: 129.28                       blocks_per_halving: 212710
# good max_supply found: 109996595.20000003 reward: 129.28                       blocks_per_halving: 212710
# good max_supply found: 109996595.20000003 reward: 129.28                       blocks_per_halving: 212710
# good max_supply found: 200001331.2000001 reward: 129.28                       blocks_per_halving: 386760
# good max_supply found: 200001331.2000001 reward: 129.28                       blocks_per_halving: 386760
# good max_supply found: 200001331.2000001 reward: 129.28                       blocks_per_halving: 386760
# good max_supply found: 200001331.2000001 reward: 129.28                       blocks_per_halving: 386760
# good max_supply found: 209997260.8 reward: 129.28                       blocks_per_halving: 406090
# good max_supply found: 209997260.8 reward: 129.28                       blocks_per_halving: 406090
# good max_supply found: 209997260.8 reward: 129.28                       blocks_per_halving: 406090
# good max_supply found: 209997260.8 reward: 129.28                       blocks_per_halving: 406090
# good max_supply found: 300001996.8000002 reward: 129.28                       blocks_per_halving: 580140
# good max_supply found: 300001996.8000002 reward: 129.28                       blocks_per_halving: 580140
# good max_supply found: 300001996.8000002 reward: 129.28                       blocks_per_halving: 580140
# good max_supply found: 300001996.8000002 reward: 129.28                       blocks_per_halving: 580140
# good max_supply found: 309997926.4 reward: 129.28                       blocks_per_halving: 599470
# good max_supply found: 309997926.4 reward: 129.28                       blocks_per_halving: 599470
# good max_supply found: 309997926.4 reward: 129.28                       blocks_per_halving: 599470
# good max_supply found: 309997926.4 reward: 129.28                       blocks_per_halving: 599470
# good max_supply found: 20002201.599999994 reward: 258.56                       blocks_per_halving: 19340
# good max_supply found: 20002201.599999994 reward: 258.56                       blocks_per_halving: 19340
# good max_supply found: 20002201.599999994 reward: 258.56                       blocks_per_halving: 19340
# good max_supply found: 20002201.599999994 reward: 258.56                       blocks_per_halving: 19340
# good max_supply found: 30003302.39999999 reward: 258.56                       blocks_per_halving: 29010
# good max_supply found: 30003302.39999999 reward: 258.56                       blocks_per_halving: 29010
# good max_supply found: 30003302.39999999 reward: 258.56                       blocks_per_halving: 29010
# good max_supply found: 30003302.39999999 reward: 258.56                       blocks_per_halving: 29010
# good max_supply found: 40004403.19999999 reward: 258.56                       blocks_per_halving: 38680
# good max_supply found: 40004403.19999999 reward: 258.56                       blocks_per_halving: 38680
# good max_supply found: 40004403.19999999 reward: 258.56                       blocks_per_halving: 38680
# good max_supply found: 40004403.19999999 reward: 258.56                       blocks_per_halving: 38680
# good max_supply found: 100000665.60000005 reward: 258.56                       blocks_per_halving: 96690
# good max_supply found: 100000665.60000005 reward: 258.56                       blocks_per_halving: 96690
# good max_supply found: 100000665.60000005 reward: 258.56                       blocks_per_halving: 96690
# good max_supply found: 100000665.60000005 reward: 258.56                       blocks_per_halving: 96690
# good max_supply found: 200001331.2000001 reward: 258.56                       blocks_per_halving: 193380
# good max_supply found: 200001331.2000001 reward: 258.56                       blocks_per_halving: 193380
# good max_supply found: 200001331.2000001 reward: 258.56                       blocks_per_halving: 193380
# good max_supply found: 200001331.2000001 reward: 258.56                       blocks_per_halving: 193380
# good max_supply found: 300001996.8000002 reward: 258.56                       blocks_per_halving: 290070
# good max_supply found: 300001996.8000002 reward: 258.56                       blocks_per_halving: 290070
# good max_supply found: 300001996.8000002 reward: 258.56                       blocks_per_halving: 290070
# good max_supply found: 300001996.8000002 reward: 258.56                       blocks_per_halving: 290070
# good max_supply found: 400002662.4000002 reward: 258.56                       blocks_per_halving: 386760
# good max_supply found: 400002662.4000002 reward: 258.56                       blocks_per_halving: 386760
# good max_supply found: 400002662.4000002 reward: 258.56                       blocks_per_halving: 386760
# good max_supply found: 400002662.4000002 reward: 258.56                       blocks_per_halving: 386760
# good max_supply found: 500003328.0000002 reward: 258.56                       blocks_per_halving: 483450
# good max_supply found: 500003328.0000002 reward: 258.56                       blocks_per_halving: 483450
# good max_supply found: 500003328.0000002 reward: 258.56                       blocks_per_halving: 483450
# good max_supply found: 500003328.0000002 reward: 258.56                       blocks_per_halving: 483450
# good max_supply found: 600003993.6000004 reward: 258.56                       blocks_per_halving: 580140
# good max_supply found: 600003993.6000004 reward: 258.56                       blocks_per_halving: 580140
# good max_supply found: 600003993.6000004 reward: 258.56                       blocks_per_halving: 580140
# good max_supply found: 600003993.6000004 reward: 258.56                       blocks_per_halving: 580140
# good max_supply found: 40004403.19999999 reward: 517.12                       blocks_per_halving: 19340
# good max_supply found: 40004403.19999999 reward: 517.12                       blocks_per_halving: 19340
# good max_supply found: 40004403.19999999 reward: 517.12                       blocks_per_halving: 19340
# good max_supply found: 40004403.19999999 reward: 517.12                       blocks_per_halving: 19340
# good max_supply found: 200001331.2000001 reward: 517.12                       blocks_per_halving: 96690
# good max_supply found: 200001331.2000001 reward: 517.12                       blocks_per_halving: 96690
# good max_supply found: 200001331.2000001 reward: 517.12                       blocks_per_halving: 96690
# good max_supply found: 200001331.2000001 reward: 517.12                       blocks_per_halving: 96690
# good max_supply found: 400002662.4000002 reward: 517.12                       blocks_per_halving: 193380
# good max_supply found: 400002662.4000002 reward: 517.12                       blocks_per_halving: 193380
# good max_supply found: 400002662.4000002 reward: 517.12                       blocks_per_halving: 193380
# good max_supply found: 400002662.4000002 reward: 517.12                       blocks_per_halving: 193380
# good max_supply found: 600003993.6000004 reward: 517.12                       blocks_per_halving: 290070
# good max_supply found: 600003993.6000004 reward: 517.12                       blocks_per_halving: 290070
# good max_supply found: 600003993.6000004 reward: 517.12                       blocks_per_halving: 290070
# good max_supply found: 600003993.6000004 reward: 517.12                       blocks_per_halving: 290070
# good max_supply found: 809996083.1999999 reward: 517.12                       blocks_per_halving: 391590
# good max_supply found: 809996083.1999999 reward: 517.12                       blocks_per_halving: 391590
# good max_supply found: 809996083.1999999 reward: 517.12                       blocks_per_halving: 391590
# good max_supply found: 809996083.1999999 reward: 517.12                       blocks_per_halving: 391590
# good max_supply found: 1009997414.3999999 reward: 517.12                       blocks_per_halving: 488280
# good max_supply found: 1009997414.3999999 reward: 517.12                       blocks_per_halving: 488280
# good max_supply found: 1009997414.3999999 reward: 517.12                       blocks_per_halving: 488280
# good max_supply found: 1009997414.3999999 reward: 517.12                       blocks_per_halving: 488280
# good max_supply found: 1029999615.9999996 reward: 517.12                       blocks_per_halving: 497950
# good max_supply found: 1029999615.9999996 reward: 517.12                       blocks_per_halving: 497950
# good max_supply found: 1029999615.9999996 reward: 517.12                       blocks_per_halving: 497950
# good max_supply found: 1029999615.9999996 reward: 517.12                       blocks_per_halving: 497950
# good max_supply found: 1050001817.6000001 reward: 517.12                       blocks_per_halving: 507620
# good max_supply found: 1050001817.6000001 reward: 517.12                       blocks_per_halving: 507620
# good max_supply found: 1050001817.6000001 reward: 517.12                       blocks_per_halving: 507620
# good max_supply found: 1050001817.6000001 reward: 517.12                       blocks_per_halving: 507620
# good max_supply found: 1070004019.2 reward: 517.12                       blocks_per_halving: 517290
# good max_supply found: 1070004019.2 reward: 517.12                       blocks_per_halving: 517290
# good max_supply found: 1070004019.2 reward: 517.12                       blocks_per_halving: 517290
# good max_supply found: 1070004019.2 reward: 517.12                       blocks_per_halving: 517290
# good max_supply found: 1099996979.2000008 reward: 517.12                       blocks_per_halving: 531790
# good max_supply found: 1099996979.2000008 reward: 517.12                       blocks_per_halving: 531790
# good max_supply found: 1099996979.2000008 reward: 517.12                       blocks_per_halving: 531790
# good max_supply found: 1099996979.2000008 reward: 517.12                       blocks_per_halving: 531790
# good max_supply found: 400002662.4000002 reward: 1034.24                       blocks_per_halving: 96690
# good max_supply found: 400002662.4000002 reward: 1034.24                       blocks_per_halving: 96690
# good max_supply found: 400002662.4000002 reward: 1034.24                       blocks_per_halving: 96690
# good max_supply found: 400002662.4000002 reward: 1034.24                       blocks_per_halving: 96690
# good max_supply found: 1009997414.3999999 reward: 1034.24                       blocks_per_halving: 244140
# good max_supply found: 1009997414.3999999 reward: 1034.24                       blocks_per_halving: 244140
# good max_supply found: 1009997414.3999999 reward: 1034.24                       blocks_per_halving: 244140
# good max_supply found: 1009997414.3999999 reward: 1034.24                       blocks_per_halving: 244140
# good max_supply found: 1050001817.6000001 reward: 1034.24                       blocks_per_halving: 253810
# good max_supply found: 1050001817.6000001 reward: 1034.24                       blocks_per_halving: 253810
# good max_supply found: 1050001817.6000001 reward: 1034.24                       blocks_per_halving: 253810
# good max_supply found: 1050001817.6000001 reward: 1034.24                       blocks_per_halving: 253810
# good max_supply found: 2059999231.9999993 reward: 1034.24                       blocks_per_halving: 497950# good max_supply found: 2059999231.9999993 reward: 1034.24                       blocks_per_halving: 497950# good max_supply found: 2059999231.9999993 reward: 1034.24                       blocks_per_halving: 497950# good max_supply found: 2059999231.9999993 reward: 1034.24                       blocks_per_halving: 497950