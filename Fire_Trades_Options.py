from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from threading import Timer


class TradeFire(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)
        self.done = False
        self.nextOrderId = ""

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId):
        self.nextOrderId = orderId
        self.start()

    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId,
                    whyHeld, mktCapPrice):
        print("OrderStatus. Id: ", orderId, ", Status: ", status, ", Filled:", filled, ", Remaining: ", remaining,
              ", LastFillPrice: ", lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print("OpenOrder. ID:", orderId, contract.symbol, contract.secType, "@", contract.exchange, ":", order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print("ExecDetails. ", reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.shares, execution.lastLiquidity)


    def start(self):
        contract = Contract()
        contract.symbol = "TQQQ"
        contract.secType = "OPT"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.lastTradeDateOrContractMonth = "20201204"
        contract.strike = 150
        contract.right = "C"
        contract.multiplier = "100"
        order = Order()
        order.action = "SELL"
        order.totalQuantity = 1
        order.orderType = "MKT"
        #order.orderType = "LMT"
        #order.lmtPrice = 500
        self.placeOrder(self.nextOrderId, contract, order)

    def stop(self):
        self.done = True
        self.disconnect()


def main():
    app = TradeFire()
    app.nextOrderId = 0
    # app.connect("127.0.0.1", 7497, 9) # TWS Live Money Account
    app.connect("127.0.0.1", 7497, 9)  # IB Gateway PaperTrading
    Timer(3, app.stop).start()
    app.run()


if __name__ == "__main__":
    main()