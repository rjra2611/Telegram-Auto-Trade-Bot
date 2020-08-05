from telegram.ext import Updater
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import datetime
import pdb
import gizoogle
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import BaseFilter
import telegram
import mysql.connector
import time
import math

print('getting bot')
telegram_token = '938075561:AAEfv4Mcm9qOW3_EPgCy770usqDdAL8I34M'
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher
bot = telegram.Bot(token=telegram_token)

kws = ""
kite = ""
login_flag = 0
database_flag = 0
telegram_flag = 0

names_list = ['3mindia', '63moons', 'aartiind', 'aban', 'abb', 'abfrl', 'acc', 'ace', 'adanient', 'adaniports', 'adanipower', 'aiaeng', 'ajantpharm', 'akzoindia', 'albk', 'alkem', 'allcargo', 'amarajabat', 'ambujacem', 'anantraj', 'apollohosp', 'apollotyre', 'arvind', 'asahiindia', 'ashokley', 'asianpaint', 'astrazen', 'atfl', 'atul', 'aubank', 'auropharma', 'autoaxles', 'avantifeed', 'axisbank', 'bajaj-auto', 'bajajelec', 'bajajfinsv', 'bajajhldng', 'bajfinance', 'balkrisind', 'balramchin', 'bancoindia', 'bankbaroda', 'bankbees', 'bankindia', 'bataindia', 'bbtc', 'bel', 'beml', 'bergepaint', 'bfutilitie', 'bharatfin', 'bharatforg', 'bhartiartl', 'bhel', 'biocon', 'blissgvs', 'blkashyap', 'bluedart', 'boschltd', 'bpcl', 'britannia', 'bse', 'cadilahc', 'camlinfine', 'canbk', 'canfinhome', 'capacite', 'castrolind', 'cdsl', 'ceatltd', 'centrum', 'centuryply', 'centurytex', 'cerebraint', 'cesc', 'cgcl', 'cgpower', 'chennpetro', 'cholafin', 'cipla', 'cnovapetro', 'coalindia', 'cochinship', 'coffeeday', 'colpal', 'concor', 'coromandel', 'cox&kings', 'crisil', 'crompton', 'cub', 'cumminsind', 'cyient', 'daawat', 'dabur', 'dalmiasug', 'dbcorp', 'dbl', 'dcbbank', 'dcmshriram', 'deltacorp', 'den', 'dhampursug', 'dhfl', 'diamondyd', 'dishtv', 'divislab', 'dixon', 'dlf', 'dmart', 'dolphinoff', 'dredgecorp', 'drreddy', 'eclerx', 'eichermot', 'eidparry', 'eihotel', 'electcast', 'emamiltd', 'endurance', 'enginersin', 'equitas', 'eris', 'erosmedia', 'escorts', 'ester', 'eveready', 'exideind', 'federalbnk', 'fel', 'fincables', 'fortis', 'fretail', 'gail', 'ganecos', 'gati', 'gdl', 'gepil', 'geship', 'get&d', 'ghcl', 'gichsgfin', 'gicre', 'gillette', 'glaxo', 'glenmark', 'globusspr', 'gmbrew', 'gmrinfra', 'gna', 'gnfc', 'godfryphlp', 'godrejagro', 'godrejcp', 'godrejind', 'godrejprop', 'goldbees', 'gppl', 'granules', 'grasim', 'greavescot', 'gsfc', 'gskcons', 'gspl', 'gss', 'gujalkali', 'gujfluoro', 'gujgasltd', 'hathway', 'havells', 'hblpower', 'hcl-insys', 'hcltech', 'hdfc', 'hdfcamc', 'hdfcbank', 'hdfclife', 'heidelberg', 'heromotoco', 'hexaware', 'hgs', 'hikal', 'hindalco', 'hindcopper', 'hindpetro', 'hindunilvr', 'hindzinc', 'honaut', 'hscl', 'hsil', 'hudco', 'ibulhsgfin', 'icicibank', 'icicigi', 'icicinifty', 'icicipruli', 'idbi', 'idea', 'idfc', 'idfcfirstb', 'iex', 'ifci', 'igl', 'indhotel', 'indiacem', 'indianb', 'indigo', 'indusindbk', 'infibeam', 'infratel', 'infy', 'inoxleisur', 'inoxwind', 'intellect', 'iob', 'ioc', 'ipcalab', 'irb', 'itc', 'itdcem', 'jagran', 'jaicorpltd', 'jamnaauto', 'jayagrogn', 'jaysreetea', 'jetairways', 'jindalstel', 'jindworld', 'jisljaleqs', 'jkcement', 'jkpaper', 'jktyre', 'jmfinancil', 'jpassociat', 'jslhisar', 'jswenergy', 'jswsteel', 'jubilant', 'jublfood', 'justdial', 'jyothylab', 'kajariacer', 'kalpatpowr',
              'kansainer', 'karurvysya', 'kec', 'kei', 'khadim', 'kilitch', 'kiriindus', 'kotakbank', 'kotaknifty', 'kscl', 'ktkbank', 'l&tfh', 'lalpathlab', 'libertshoe', 'lichsgfin', 'lincoln', 'liquidbees', 'lovable', 'lt', 'lupin', 'm&m', 'm&mfin', 'm50', 'magma', 'mahindcie', 'mahlog', 'mahseamles', 'majesco', 'manalipetc', 'manappuram', 'mangtimber', 'maninds', 'maninfra', 'marico', 'marksans', 'maruti', 'masfin', 'mastek', 'matrimony', 'mcdowell-n', 'mcleodruss', 'mcx', 'megh', 'mfsl', 'mgl', 'midhani', 'mindacorp', 'mindaind', 'mindtree', 'mmtc', 'moil', 'moldtkpac', 'morepenlab', 'mothersumi', 'mphasis', 'mrf', 'mrpl', 'mukandltd', 'munjalau', 'muthootfin', 'natcopharm', 'nationalum', 'naukri', 'navinfluor', 'navnetedul', 'nbcc', 'ncc', 'nestleind', 'network18', 'nfl', 'nh', 'nhpc', 'niacl', 'niftybees', 'niitltd', 'niittech', 'nlcindia', 'nmdc', 'nocil', 'nrbbearing', 'ntpc', 'oberoirlty', 'ofss', 'oil', 'omaxe', 'ongc', 'orientbank', 'orientcem', 'pageind', 'paperprod', 'paragmilk', 'pateleng', 'pcjeweller', 'pel', 'persistent', 'petronet', 'pfc', 'pfizer', 'pghh', 'philipcarb', 'phoenixltd', 'pidilitind', 'piind', 'pnb', 'pnbgilts', 'pnbhousing', 'polyplex', 'powergrid', 'prajind', 'prestige', 'ptc', 'purva', 'pvr', 'quickheal', 'radico', 'radiocity', 'rajeshexpo', 'rallis', 'ramcocem', 'ramcoind', 'ramky', 'raymond', 'rblbank', 'rcf', 'recltd', 'relaxo', 'relcapital', 'reliance', 'relinfra', 'repcohome', 'ricoauto', 'riil', 'rkforge', 'rpower', 'sadbhav', 'sail', 'sakuma', 'salasar', 'salzerelec', 'sanghiind', 'sanghvimov', 'sanofi', 'saregama', 'satin', 'sbilife', 'sbin', 'schaeffler', 'schand', 'schneider', 'sci', 'selan', 'sequent', 'shardamotr', 'shreecem', 'shriramcit', 'siemens', 'simplexinf', 'sintex', 'sis', 'sjvn', 'skfindia', 'snowman', 'sobha', 'solarinds', 'southbank', 'sparc', 'sptl', 'sreinfra', 'srf', 'srtransfin', 'star', 'stcindia', 'strtech', 'sundarmfin', 'sundrmfast', 'sunpharma', 'sunteck', 'suntv', 'supremeind', 'suven', 'suzlon', 'syndibank', 'syngene', 'take', 'talwalkars', 'tanla', 'tatachem', 'tatacoffee', 'tatacomm', 'tataelxsi', 'tataglobal', 'tatainvest', 'tatamotors', 'tatamtrdvr', 'tatapower', 'tatasponge', 'tatasteel', 'tbz', 'tci', 'tcs', 'techm', 'tejasnet', 'texmopipes', 'texrail', 'thermax', 'thomascook', 'thyrocare', 'tifin', 'timetechno', 'tinplate', 'titan', 'tnpetro', 'tnpl', 'torntpharm', 'torntpower', 'trent', 'trident', 'trigyn', 'triveni', 'ttkprestig', 'tv18brdcst', 'tvsmotor', 'twl', 'ubl', 'ucobank', 'ujjivan', 'ultracemco', 'unionbank', 'univcables', 'upl', 'ushamart', 'vedl', 'vguard', 'vijayabank', 'vipclothng', 'vipind', 'voltas', 'vtl', 'wabcoindia', 'walchannag', 'welcorp', 'welent', 'welspunind', 'whirlpool', 'windmachin', 'wipro', 'wockpharma', 'wonderla', 'yesbank', 'zeel']


api_k = "Enter your api key"  # id
api_s = "Enter your secret key"  # pass
quantity = 1


# starttime = now.replace(hour=9, minute=14, second=57, microsecond=0)  #ist
# endtime = now.replace(hour=15, minute=0, second=0, microsecond=0)
# starttime = now.replace(hour=18, minute=0, second=57, microsecond=0)  # utc
# endtime = now.replace(hour=23, minute=30, second=0, microsecond=0)

def buy_order_limit_BO(name, price, quantity, target, sl):
    print("placing buy order with name quantity sl price",
          name, price, quantity, target, sl)

    kite.place_order(tradingsymbol=name, price=price, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=quantity, trigger_price=price, order_type=kite.ORDER_TYPE_SL, product=kite.PRODUCT_MIS)

    kite.place_order(tradingsymbol=name, price=sl, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=quantity, trigger_price=sl, order_type=kite.ORDER_TYPE_SL,
                     product=kite.PRODUCT_MIS)

    kite.place_order(tradingsymbol=name, price=target, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=quantity, order_type=kite.ORDER_TYPE_LIMIT, product=kite.PRODUCT_MIS)


def sell_order_limit_BO(name, price, quantity, target, sl):
    print("placing sell order with name quantity sl price",
          name, price, quantity, target, sl)

    kite.place_order(tradingsymbol=name, price=price, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=quantity, trigger_price=price, order_type=kite.ORDER_TYPE_SL, product=kite.PRODUCT_MIS)

    kite.place_order(tradingsymbol=name, price=sl, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=quantity, trigger_price=sl, order_type=kite.ORDER_TYPE_SL,
                     product=kite.PRODUCT_MIS)

    kite.place_order(tradingsymbol=name, price=target, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=quantity, order_type=kite.ORDER_TYPE_LIMIT, product=kite.PRODUCT_MIS)


def buy_order_market_CO(name, quantity, sl):
    print("placing order with name quantity sl price", name, quantity, sl)
    # trd_portfolio[inst_of_single_company]['status'] = "bought"
    kite.place_order(tradingsymbol=name, variety=kite.VARIETY_CO, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=quantity, trigger_price=sl, order_type=kite.ORDER_TYPE_MARKET, product=kite.PRODUCT_MIS)
    # trd_portfolio[inst_of_single_company]["order_ids"] = order_id


def sell_order_market_CO(name, quantity, sl):
    print("placing order with name quantity sl price", name, quantity, sl)
    # trd_portfolio[inst_of_single_company]['status'] = "sold"
    kite.place_order(tradingsymbol=name, variety=kite.VARIETY_CO, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_SELL, trigger_price=sl, quantity=quantity, order_type=kite.ORDER_TYPE_MARKET, product=kite.PRODUCT_MIS)
    # trd_portfolio[inst_of_single_company]["order_ids"] = order_id


def update_access_token(new_token):
    try:
        print("updating access token")
        sql = "update token_val set value=%s where name=%s "
        val = (new_token, 'access_token')
        mycursor.execute(sql, val)
        mydb.commit()
    except Exception as e:
        bot.sendMessage(chat_id=984101934, text=e)
        print(e)


def get_access_token(request_tkn):
    try:
        print("getting access token...")
        kite = KiteConnect(api_key=api_k)
        data = kite.generate_session(request_tkn, api_secret=api_s)
        access_token = data["access_token"]
        kite.set_access_token(access_token)
        return access_token
    except Exception as e:
        bot.sendMessage(chat_id=984101934, text=e)
        print(e)


def fetch_access_token():
    try:
        print("fetching access token value")
        mycursor.execute("select value from token_val")
        myresult = mycursor.fetchone()
        for row in myresult:
            a = row
        return a
    except Exception as e:
        bot.sendMessage(chat_id=984101934, text=e)
        print(e)


def get_login(api_k, api_s):  # log in to zerodha API panel
    try:
        print("trying to login...")
        global kite, kws, login_flag
        kite = KiteConnect(api_key=api_k)
        access_token = fetch_access_token()
        kite.set_access_token(access_token)
        login_flag = 1
        bot.sendMessage(chat_id=984101934,
                        text="you are now logged in for today")
        print("you are now logged in for today")
    except Exception as e:
        bot.sendMessage(chat_id=984101934,
                        text="update api key, not able to login")
        print(e)


def start(update, context):
        # context.bot.send_message(chat_id="@algobrainTrade", text="debugging")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Mr Ronit not available, please talk to me!")


def set_token(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Permission to only Mr Ronit Jain, you can talk to me")


def update_api(update, context):
    request_token = update.message.text.split()[1]
    print("new request token is ", request_token)
    try:
        access_token = get_access_token(request_token)
        update_access_token(access_token)
        get_login(api_k, api_s)
        bot.sendMessage(chat_id=984101934, text="access token updated")
    except:
        bot.sendMessage(chat_id=984101934, text="update error")
        print('update error')


def echo(update, context):
    reply = gizoogle.text(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


class Api_filter(BaseFilter):
    def filter(self, message):
        return 'api' in message.text or 'Api' in message.text


# Remember to initialize the class.
api_filter = Api_filter()


def search_buy(msg):
    buy = {}
    msg = msg.lower()
    msg = msg.split()
    # print(msg)
    if 'buy' in msg or 'bought' in msg or '\U0001f7e2buy' in msg:
        name_findlist = msg[:msg.index("sl")]
        for name in name_findlist:
            if not len(buy.keys()):
                for val in range(len(names_list)):
                    if name in names_list[val]:
                        # print(names_list[val])
                        buy['name'] = names_list[val].upper()
                        break
        # print(buy)
        for i in msg[:msg.index("sl")]:
            try:
                i = i.split('-')[0]
                if float(i) < 10000:
                    buy['price'] = round(float(i), 2)
                    break
            except:
                continue
        # print(buy)
        if("sl" in msg):
            buy['sl'] = float(msg[msg.index("sl")+1])
            # print(buy)
            if 'target' in msg:
                buy['target'] = float(msg[msg.index("target")+1].split('/')[0])
            if 'tgt' in msg:
                buy['target'] = float(msg[msg.index("tgt")+1].split('/')[0])
            if 'tg' in msg:
                buy['target'] = float(msg[msg.index("tg")+1].split('/')[0])
            # print(buy)
        if 'above' in msg:
            buy['above'] = 'True'
    return buy


def search_sell(msg):
    sell = {}
    msg = msg.lower()
    msg = msg.split()
    # print(msg)
    if 'sell' in msg or 'sold' in msg or '\U0001f7e2short' in msg or 'short' in msg:
        name_findlist = msg[:msg.index("sl")]
        for name in name_findlist:
            if not len(sell.keys()):
                for val in range(len(names_list)):
                    if name in names_list[val]:
                        # print(names_list[val])
                        sell['name'] = names_list[val].upper()
                        break
        # print(sell)
        for i in msg[:msg.index("sl")]:
            try:
                i = i.split('-')[0]
                if float(i) < 10000:
                    sell['price'] = round(float(i), 2)
                    break
            except:
                continue
        # print(sell)
        if("sl" in msg):
            sell['sl'] = float(msg[msg.index("sl")+1])
            print(sell)
            if 'target' in msg:
                sell['target'] = float(
                    msg[msg.index("target")+1].split('/')[0])
            if 'tgt' in msg:
                sell['target'] = float(msg[msg.index("tgt")+1].split('/')[0])
            if 'tg' in msg:
                sell['target'] = float(msg[msg.index("tg")+1].split('/')[0])
            # print(sell)
        if 'below' in msg:
            sell['below'] = 'True'
    return sell


def faadoo_msges(update, context):
    try:
        print('message reveiced from faadoo')
        msg = update.message.text
        ans1 = search_buy(msg)
        ans2 = search_sell(msg)
        print("ans1:", ans1, "ans2:", ans2)

        if('name' in ans1.keys() and 'sl' in ans1.keys()):
            # print(ans1)
            bot.sendMessage(chat_id="@algobrainTrade",
                            text="buy  " + str(ans1))
            if 'above' in ans1.keys() and ans1['above']:
                try:
                    quantity = math.floor(
                        100/(abs(int(ans1['sl'])-int(ans1['price']))))
                    if('target' in ans1.keys()):
                        # buy_order_limit_BO(
                        #     ans1['name'], ans1['price'], quantity, ans1['target'], ans1['sl'])
                        pass
                    else:
                        # buy_order_limit_BO(
                        #     ans1['name'], ans1['price'], quantity, 'open', ans1['sl'])
                        pass
                except Exception as e:
                    bot.sendMessage(chat_id=984101934, text=str(e))
                    print(e)
            else:
                try:
                    # buy_order_market_CO(ans1['name'].upper(
                    # ), 5, ans1['sl'])
                    pass
                except Exception as e:
                    bot.sendMessage(chat_id=984101934, text=str(e))
                    print(e)

        if('name' in ans2.keys() and 'sl' in ans2.keys()):
            # print(ans2)
            bot.sendMessage(chat_id="@algobrainTrade",
                            text="sell  " + str(ans2))
            if 'below' in ans2.keys() and ans2['below']:
                try:
                    quantity = math.floor(
                        100/(abs(int(ans1['sl'])-int(ans1['price']))))
                    if('target' in ans2.keys()):
                        # sell_order_limit_BO(
                        #     ans2['name'], ans2['price'], quantity, ans2['target'], ans2['sl'])
                        pass
                    else:
                        # sell_order_limit_BO(
                        #     ans2['name'], ans2['price'], quantity, 'open', ans2['sl'])
                        pass
                except Exception as e:
                    bot.sendMessage(chat_id=984101934, text=str(e))
                    print(e)
            else:
                try:
                    # sell_order_market_CO(ans2['name'].upper(
                    # ), 5, ans2['sl'])
                    pass
                except Exception as e:
                    bot.sendMessage(chat_id=984101934, text=str(e))
                    print(e)
    except Exception as e:
        print(e)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

token_handler = CommandHandler('set_token', set_token)
dispatcher.add_handler(token_handler)

api_handler = MessageHandler(api_filter, update_api)
dispatcher.add_handler(api_handler)

faadoo_handler = MessageHandler(
    Filters.chat(username="@rjra2611"), faadoo_msges)
dispatcher.add_handler(faadoo_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

print('entering while loop')
while True:
    # print('a')
    now = datetime.datetime.now()
    starttime = now.replace(hour=2, minute=0, second=40, microsecond=0)  # utc
    endtime = now.replace(hour=9, minute=30, second=0, microsecond=0)
    # starttime = now.replace(hour=0, minute=1, second=57, microsecond=0)  # ist
    # endtime = now.replace(hour=23, minute=30, second=0, microsecond=0)
    if starttime <= now < endtime:
        if(not login_flag):
            print('b')
            if not database_flag:
                try:
                    if not telegram_flag:
                        updater.start_polling()
                        bot.sendMessage(chat_id=984101934,
                                        text="Bot is ready and listening...")
                        telegram_flag = 1
                    mydb = mysql.connector.connect(
                        host="database-restored1.cninlcvpipmk.us-east-1.rds.amazonaws.com", user="admin", passwd="password", database="stocks")
                    time.sleep(2)
                    mycursor = mydb.cursor()
                    print("got new connection mysql")
                    database_flag = 1
                except Exception as e:
                    bot.sendMessage(chat_id=984101934,
                                    text="database instance error")
                    print(e)
            try:
                get_login(api_k, api_s)
                print("sleeping for 10 sec before another trial")
                time.sleep(15)
            except Exception as e:
                bot.sendMessage(chat_id=984101934, text=str(e))
                print(e)
    else:
        login_flag = 0
        telegram_flag = 0
        database_flag = 0
        # print(telegram_flag,login_flag,database_flag)
