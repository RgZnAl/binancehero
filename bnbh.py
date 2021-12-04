from web3 import Web3
import json
import time
import logging
from datetime import datetime as dt
from ast import literal_eval


# bsc = "https://bsc-dataseed.binance.org/"
bsc = "https://bsc-dataseed1.defibit.io/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

bsc_acc=[
    ("account","privatekey"),
]
totalreward=0
totalwin=0
totallose=0
Claimable=0
contract_addr="0xde9ffb228c1789fef3f08014498f2b16c57db855"

abi=json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"ClaimedRewards","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroIds","type":"uint256"}],"name":"CreatedAndSendPrizeHero","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"CreatedHero","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"ExpeditedHero","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"_attackingHero","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"enemyType","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"rewards","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"xpGained","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"hpLoss","type":"uint256"}],"name":"Fight","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"MovedHeroToBag","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"TakeHeroFromBag","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"_heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"level","type":"uint256"}],"name":"UnlockedLevel","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"UpdatedBNBPoolAddress","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"UpdatedBurnAddress","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"characterAddress","type":"address"}],"name":"UpdatedCharacterContract","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"percent","type":"uint256"}],"name":"UpdatedDividePercent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"lockTime","type":"uint256"}],"name":"UpdatedFirstLockTime","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"UpdatedPriceOracle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"tokenAddress","type":"address"}],"name":"UpdatedTokenContract","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint8","name":"townType","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"level","type":"uint8"}],"name":"UpgradedTown","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"bannedList","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bnbhPool","outputs":[{"internalType":"contract IBNBHPool","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bnbhToken","outputs":[{"internalType":"contract IBEP20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"burnAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"characters","outputs":[{"internalType":"contract IBNBHCharacter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"createNewHero","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"dividePercent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"expediteHero","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"feeToLevelup","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_attackingHero","type":"uint256"},{"internalType":"uint256","name":"enemyType","type":"uint256"}],"name":"fight","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"firstLockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"bool","name":"calcTown","type":"bool"}],"name":"getHero","outputs":[{"components":[{"internalType":"uint256","name":"name","type":"uint256"},{"internalType":"uint256","name":"heroType","type":"uint256"},{"internalType":"uint256","name":"xp","type":"uint256"},{"internalType":"uint256","name":"attack","type":"uint256"},{"internalType":"uint256","name":"armor","type":"uint256"},{"internalType":"uint256","name":"speed","type":"uint256"},{"internalType":"uint256","name":"hp","type":"uint256"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"arrivalTime","type":"uint256"},{"internalType":"uint256","name":"level","type":"uint256"},{"internalType":"uint256","name":"heroClass","type":"uint256"}],"internalType":"struct HeroLibrary.Hero","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bool","name":"calcTown","type":"bool"}],"name":"getHeroesByOwner","outputs":[{"components":[{"internalType":"uint256","name":"name","type":"uint256"},{"internalType":"uint256","name":"heroType","type":"uint256"},{"internalType":"uint256","name":"xp","type":"uint256"},{"internalType":"uint256","name":"attack","type":"uint256"},{"internalType":"uint256","name":"armor","type":"uint256"},{"internalType":"uint256","name":"speed","type":"uint256"},{"internalType":"uint256","name":"hp","type":"uint256"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"arrivalTime","type":"uint256"},{"internalType":"uint256","name":"level","type":"uint256"},{"internalType":"uint256","name":"heroClass","type":"uint256"}],"internalType":"struct HeroLibrary.Hero[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getHeroesInBag","outputs":[{"components":[{"internalType":"uint256","name":"name","type":"uint256"},{"internalType":"uint256","name":"heroType","type":"uint256"},{"internalType":"uint256","name":"xp","type":"uint256"},{"internalType":"uint256","name":"attack","type":"uint256"},{"internalType":"uint256","name":"armor","type":"uint256"},{"internalType":"uint256","name":"speed","type":"uint256"},{"internalType":"uint256","name":"hp","type":"uint256"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"arrivalTime","type":"uint256"},{"internalType":"uint256","name":"level","type":"uint256"},{"internalType":"uint256","name":"heroClass","type":"uint256"}],"internalType":"struct HeroLibrary.Hero[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"getPriceToUnlockLevel","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint8","name":"townType","type":"uint8"}],"name":"getTownLevel","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getTownsOfPlayer","outputs":[{"components":[{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256","name":"lastUpgradedTimeStamp","type":"uint256"}],"internalType":"struct HeroLibrary.Town[4]","name":"","type":"tuple[4]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IBEP20","name":"_bnbhToken","type":"address"},{"internalType":"contract IBNBHCharacter","name":"_bnbhCharacter","type":"address"},{"internalType":"contract IBNBHPool","name":"_bnbhPool","type":"address"},{"internalType":"contract IPriceOracle","name":"_priceOracle","type":"address"},{"internalType":"contract IRandoms","name":"_randoms","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"maxHeroCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"}],"name":"migrateBannedList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"moveHeroToBag","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"numTokensToSend","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"priceOracle","outputs":[{"internalType":"contract IPriceOracle","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"randoms","outputs":[{"internalType":"contract IRandoms","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"sendPrizeHero","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenAddress","type":"address"}],"name":"setBNBHTokenContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"setBNBPoolAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bool","name":"status","type":"bool"}],"name":"setBannAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"setBurnAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"characterAddress","type":"address"}],"name":"setCharacterContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"percent","type":"uint256"}],"name":"setDividePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"setFeeToLvlUp","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockTime","type":"uint256"}],"name":"setFirstLockTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"setNumTokensToSend","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"setPriceOracle","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"takeHeroFromBag","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"unLockLevel","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"unLockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"townType","type":"uint8"}],"name":"upgradeTown","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')



def upgrade(heroid):
    nonce = web3.eth.getTransactionCount(me)
    print("Current nonce",nonce)
    token_tx = contract.functions.unLockLevel(heroid).buildTransaction({
    'chainId':56, 'gas': 200000,'gasPrice': web3.toWei('5.2','gwei'), 'nonce':nonce
    })
    try:
        sign_txn = web3.eth.account.signTransaction(token_tx, private_key=pvkey)
        tx_hash=web3.eth.sendRawTransaction(sign_txn.rawTransaction)
        trans=web3.toHex(tx_hash)
        print("ID %d upgrade" %(heroid))
    except IOError:
        time.sleep(100)
        sign_txn = web3.eth.account.signTransaction(token_tx, private_key=pvkey)
        tx_hash=web3.eth.sendRawTransaction(sign_txn.rawTransaction)
        trans=web3.toHex(tx_hash)
        print("get hash error retry")
        transaction=web3.eth.get_transaction(trans)
    else:
        time.sleep(10)
        trans_result = web3.eth.waitForTransactionReceipt(tx_hash,timeout=60,poll_latency=0.1)
        trans_result=web3.toJSON(trans_result)
        trans_result_status=json.loads(trans_result)['status']
        print(trans_result_status)
        if trans_result_status==0:
            print("Trans failed")

def heroFight(heroid,stage):
    global totalreward
    global totalwin
    global totallose
    nonce = web3.eth.getTransactionCount(me)
    print("Current nonce",nonce)
    token_tx = contract.functions.fight(heroid,stage).buildTransaction({
    'chainId':56, 'gas': 200000,'gasPrice': web3.toWei('5.2','gwei'), 'nonce':nonce
    })
    try:
        sign_txn = web3.eth.account.signTransaction(token_tx, private_key=pvkey)
        tx_hash=web3.eth.sendRawTransaction(sign_txn.rawTransaction)
        trans=web3.toHex(tx_hash)
        print("ID %d fight stage %d tx:%s"%(heroid,stage,trans))
    except IOError:
        time.sleep(100)
        sign_txn = web3.eth.account.signTransaction(token_tx, private_key=pvkey)
        tx_hash=web3.eth.sendRawTransaction(sign_txn.rawTransaction)
        trans=web3.toHex(tx_hash)
        print("get hash error retry")
        transaction=web3.eth.get_transaction(trans)
    else:
        time.sleep(10)
        trans_result = web3.eth.waitForTransactionReceipt(tx_hash,timeout=120,poll_latency=0.1)
        trans_result=web3.toJSON(trans_result)
        trans_result_status=json.loads(trans_result)['status']
        logs=json.loads(trans_result)['logs'][0]
        logdata=logs.get('data')
        logdata = literal_eval(logdata)
        hplose=logdata&0xff
        expgain=(logdata>>(64*4))&0xfff
        bnbreward=(logdata>>(128*4))&0xffffffffffffffffffff
        bnbreward=web3.fromWei(bnbreward, 'ether')
        totalreward+=bnbreward
        if hplose == 200:
            totallose+=1
        else:
            totalwin+=1
        print("hp lose : %d exp: %d rewards: %lf" %(int(hplose),int(expgain),float(bnbreward)))
        # print(trans_result_status)
        if trans_result_status==0:
            print("Trans failed")

start=dt.now()

# get heroes
while 1:


    for acc in range(len(bsc_acc)):
        try:
            me=bsc_acc[acc][0]
            pvkey=bsc_acc[acc][1]
            print("Address [%s]"% (me))
            contract = web3.eth.contract(address=Web3.toChecksumAddress(contract_addr), abi=abi)
            bal = contract.functions.balances(me).call()


            Claimable+=bal
            heroes = contract.functions.getHeroesByOwner(me,True).call()
            heroes_count=len(heroes)
        except:
            continue
        for i in range(0,heroes_count):
            try:
                print("Hero: #%6d Level:%2d Exp:%6d Hp:%4d "% (heroes[i][7],heroes[i][9],heroes[i][2],heroes[i][6]))
                heroExp=heroes[i][2]
                hId=heroes[i][7]
                heroHp=heroes[i][6]
                if heroExp % 1000 == 999:
                    upgrade(hId)
                elif heroHp > 200:
                    heroFight(hId,5)
                else:
                    print("No HP to fight")
                time.sleep(5)
            except:
                continue
        print("\n")
    runtime=dt.now()-start
    print("RunTime",runtime)
    print("Win:%3d Lose:%3d  Total Reward %lf Claimable %lf"%(totalwin,totallose,totalreward,web3.fromWei(Claimable,'ether')))
   
    print("\n")
    Claimable = 0
    time.sleep(60)

