from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from threading import Timer

#get greeks
class GettheGreeks(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)
        self.done = False
        self.nextOrderId = ""

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId):
        self.nextOrderId = orderId
        self.start()


    def tickOptionComputation(self, reqId: TickerId, tickType: TickType, tickAttrib: int,
                              impliedVol: float, delta: float, optPrice: float, pvDividend: float,
                              gamma: float, vega: float, theta: float, undPrice: float):
        super().tickOptionComputation(reqId, tickType, tickAttrib, impliedVol, delta,
                                      optPrice, pvDividend, gamma, vega, theta, undPrice)

        print("TickOptionComputation. TickerId:", reqId, "TickType:", tickType,
              "TickAttrib:", tickAttrib, "ImpliedVolatility:", impliedVol, "Delta:", delta, "OptionPrice:",
              optPrice, "pvDividend:", pvDividend, "Gamma: ", gamma, "Vega:", vega,
              "Theta:", theta, "UnderlyingPrice:", undPrice)

        def start(self):
            def start(self):
                # define the contract
                contract = Contract()
                contract.symbol = "TQQQ"
                contract.secType = "OPT"
                contract.exchange = "SMART"
                contract.currency = "USD"
                contract.lastTradeDateOrContractMonth = "20201204"
                contract.strike = 150
                contract.right = "C"
                contract.multiplier = "100"
                self.reqMktData(1013, ContractSamples.OptionWithLocalSymbol(), "", False, False, [])

        def stop(self):
            self.reqMktData(1013, ContractSamples.OptionWithLocalSymbol(), "", False, False, [])
            self.done = True
            self.disconnect()


#execute the classes
def main():
    app = GettheGreeks()
    appnextOrderId = 0
    app.connect("127.0.0.1", 7497, 9)  # IB Gateway PaperTrading
    Timer(3, app.stop).start()
    app.run()

if __name__ == "__main__":
    main()