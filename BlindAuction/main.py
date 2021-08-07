from replit import clear
from art import logo
morebidders = True

bids = {}
# bids = {'adam': '123', 'mason': '321', 'addie': '234'}
def highestbidder():
    highbid = 0
    highbidder = ""
    # print(bids)

    for key in bids:
        if int(bids[key]) >= int(highbid):
            highbid = bids[key]
            highbidder = key
    print(logo)
    print(f"Highest Bidder is: {highbidder} at ${highbid}")



while morebidders:
    print(logo)
    nameinput = input("What is your name: ")
    yourbid = input("How much do you bid? $")

    bids[nameinput] = yourbid
    morebidders = input("Any more bidders? y/n? ")
    if morebidders.lower() == "y":
        clear()
        continue
    elif morebidders.lower() == "n":
        clear()
        morebidders = False


highestbidder()

