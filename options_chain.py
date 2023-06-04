from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Timer

class TestApp(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId):
        self.start()

    def contractDetails(self, reqID, contractDetails):
        print("contractDetails: ", reqID, " ", contractDetails, "\n")

    def contractDetailsEnd(self, reqId):
        print("\ncontractDetails End\n")

    def start(self):
        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "OPT"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.lastTradeDateOrContractMonth = "20201211"

        self.reqContractDetails(1, contract)

    def stop(self):
        self.done = True
        self.disconnect()

def main():
    app = TestApp()
    app.nextOrderID = 0
    app.connect("127.0.0.1", 7497, 0)

    Timer(4, app.stop).start()
    app.run()

if __name__ == "__main__":
    main()
