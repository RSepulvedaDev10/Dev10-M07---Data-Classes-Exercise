from dataclasses import dataclass, field
import datetime

@dataclass
class Orders:

    OrderID: int
    CustomerID: int
    SalespersonPersonID: int
    PickedByPersonID: int
    ContactPersonID: int
    BackorderOrderID: int
    OrderDate: datetime.date
    ExpectedDeliveryDate: datetime.date
    IsUnderSupplyBackordered: bool
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    PickingCompletedWhen: datetime.datetime
    LastEditedBy: int
    LastEditedWhen: datetime.datetime
    
    def __gt__(self, other):
        if self.OrderDate > other.OrderDate:
            print(True)
        else:
            print(False)
    
    def __ge__(self, other):
        if self.OrderDate >= other.OrderDate:
            print(True)
        else:
            print(False)
    
    def __eq__(self, other):
        if self.CustomerID == other.CustomerID:
            print(True)
        else:
            print(False)

@dataclass
class Invoices:
    
    InvoiceID: int
    CustomerID: int
    BilltoCustomerID: int
    OrderID: int
    DeliveryMethodID: int
    ContactPersonID: int
    AccountsPersonID: int
    SalesPersonPersonID: int
    PackedByPersonID: int
    InvoiceDate: datetime.datetime
    CustomerPurchaseOrderNumber: str
    IsCreditNote: bool
    CreditNoteReason: str
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    TotalDryItems: int
    TotalChillerItems: int
    DeliveryRun: str
    RunPosition: bool
    ReturnedDeliveryData: str
    ConfirmedDeliveryTime: datetime.datetime
    ConfirmedRecievedBy: str
    LastEditedBy: int
    LastEditedWhen: datetime.datetime 
    
    def __gt__(self, other):
        if self.TotalDryItems > other.TotalDryItems:
            print(True)
        else:
            print(False)
    
    def __ge__(self, other):
        if self.TotalDryItems >= other.TotalDryItems:
            print(True)
        else:
            print(False)
    
    def __eq__(self, other):
        if self.ContactPersonID == other.ContactPersonID:
            print(True)
        else:
            print(False)

@dataclass
class Customers:
    
    CustomerID: int
    CustomerName: str
    BillToCustomerID: int
    CustomerCategoryID: int
    BuyingGroupID: int
    PrimaryContactPersonID: int
    AlternateContactPersonID: int
    DeliveryMethodID: int
    DeliveryCityID: int
    PostalCityID: int
    CreditLimit: float
    AccountOpenedDate: datetime.datetime
    StandardDiscountPercentage: float
    IsStatementSent: bool
    IsOnCreditHold: bool
    PaymentDays: int
    PhoneNumber: str
    FaxNumber: str
    DeliveryRun: str
    RunPostion: bool
    WebsiteURL: str
    DeliveryAddressLine1: str
    DeliveryAddressLine2: str
    DeliveryPostalCode: str
    DeliveryLocation: str
    PostalAddressLine1: str
    PostalAddressLine2: str
    PostalPostalCode: str
    LastEditedBy: int
    ValidFrom: datetime.datetime
    ValidTo: datetime.datetime
    
