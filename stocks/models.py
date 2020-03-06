from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel

# Create your models here.
class Company(SoftDeletableModel, TimeStampedModel):
    Symbol = models.CharField(_('ICBCode'), max_length=255, blank=True) # "FPT"
    ICBCode = models.CharField(_('ICBCode'), max_length=255, blank=True) # "9537"
    CompanyName = models.CharField(_('CompanyName'), max_length=255, blank=True) # "CTCP FPT"
    ShortName = models.CharField(_('ShortName'), max_length=255, blank=True) # "FPT Corp"
    InternationalName = models.CharField(_('InternationalName'), max_length=255, blank=True) # "FPT Corporation"
    HeadQuarters = models.CharField(_('HeadQuarters'), max_length=255, blank=True) # "Số 17, Phố Duy Tân, Phường Dịch vọng Hậu, Quận C..."
    Phone = models.CharField(_('Phone'), max_length=255, blank=True) # "+84 (24) 730-07300"
    Fax = models.CharField(_('Fax'), max_length=255, blank=True) # "+84 (24) 376-87410"
    Email = models.CharField(_('Email'), max_length=255, blank=True) # null
    WebAddress = models.CharField(_('WebAddress'), max_length=255, blank=True) # "www.fpt.com.vn"
    Overview = models.TextField(_('Overview'), blank=True) # "Nhiều năm gần đây, Công ty FPT được bình chọn là Công ty tin họ"
    History = models.TextField(_('History'), blank=True) # "<div>↵<ul>↵	<li>Ngày 13/9/1988, thành lập Công"
    BusinessAreas = models.TextField(_('BusinessAreas'), blank=True) # ""<ul>↵	<li style="text-align:justify"><span style="font-size:12px">Xây "
    Employees = models.CharField(_('Employees'), max_length=255, blank=True) # 11556
    Branches = models.CharField(_('Branches'), max_length=255, blank=True) # 17
    EstablishmentDate = models.CharField(_('EstablishmentDate'), max_length=255, blank=True) # "1988-09-13T00:00:00"
    BusinessLicenseNumber = models.CharField(_('BusinessLicenseNumber'), max_length=255, blank=True) # "0101248141 "
    DateOfIssue = models.CharField(_('DateOfIssue'), max_length=255, blank=True) # "2019-06-11T00:00:00"
    TaxIDNumber = models.CharField(_('TaxIDNumber'), max_length=255, blank=True) # "0101248141"
    CharterCapital = models.CharField(_('CharterCapital'), max_length=255, blank=True) # 6783586880000
    DateOfListing = models.CharField(_('DateOfListing'), max_length=255, blank=True) # "2006-11-21T00:00:00"
    Exchange = models.CharField(_('Exchange'), max_length=255, blank=True) # "HSX"
    InitialListingPrice = models.CharField(_('InitialListingPrice'), max_length=255, blank=True) # 400000
    ListingVolume = models.CharField(_('ListingVolume'), max_length=255, blank=True) # 678358688
    StateOwnership = models.CharField(_('StateOwnership'), max_length=255, blank=True) # 0.0596
    ForeignOwnership = models.CharField(_('ForeignOwnership'), max_length=255, blank=True) # 0.489999988206829
    OtherOwnership = models.CharField(_('OtherOwnership'), max_length=255, blank=True) # 0.450400011793171
    IsListed = models.CharField(_('IsListed'), max_length=255, blank=True) # true

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('Company')
        verbosee_name_plural = _('Companies')

    def __str__(self):
        return self.get_InternationalName

    @property
    def get_InternationalName(self):
        return self.InternationalName


class LatestFinancialInfo(SoftDeletableModel, TimeStampedModel):
    Symbol = models.CharField(_('Symbol'), max_length=255, blank=True) # "AAV"
    LFY = models.CharField(_('LFY'), max_length=255, blank=True) # 2019
    Year = models.CharField(_('Year'), max_length=255, blank=True) # 2019
    Quarter = models.CharField(_('Quarter'), max_length=255, blank=True) # 4
    Date = models.CharField(_('Date'), max_length=255, blank=True) # "2020-02-28T00:00:00"
    BookValuePerShare = models.CharField(_('BookValuePerShare'), max_length=255, blank=True) # 11702.509126369772
    SalesPerShare = models.CharField(_('SalesPerShare'), max_length=255, blank=True) # 20154.73321956038
    SharesOutstanding = models.CharField(_('SharesOutstanding'), max_length=255, blank=True) # 31874996
    MarketCapitalization = models.CharField(_('MarketCapitalization'), max_length=255, blank=True) # 216749972800
    PE = models.CharField(_('PE'), max_length=255, blank=True) # 7.418466458401749
    BasicPE = models.CharField(_('BasicPE'), max_length=255, blank=True) # 6.321920625456336
    DilutedPE = models.CharField(_('DilutedPE'), max_length=255, blank=True) # 7.418466458401749
    PB = models.CharField(_('PB'), max_length=255, blank=True) # 0.6448342217424873
    PS = models.CharField(_('PS'), max_length=255, blank=True) # 0.3373897300412058
    EPS = models.CharField(_('EPS'), max_length=255, blank=True) # 916.6314949498346
    BasicEPS = models.CharField(_('BasicEPS'), max_length=255, blank=True) # 1075.6224892509078
    DilutedEPS = models.CharField(_('DilutedEPS'), max_length=255, blank=True) # 916.6314949498346
    GrossMargin = models.CharField(_('GrossMargin'), max_length=255, blank=True) # 0.10473504596460788
    EBITMargin = models.CharField(_('EBITMargin'), max_length=255, blank=True) # 0.07239285911743792
    OperatingMargin = models.CharField(_('OperatingMargin'), max_length=255, blank=True) # 0.07361468044530914
    QuickRatio = models.CharField(_('QuickRatio'), max_length=255, blank=True) # 1.8344993380381511
    CurrentRatio = models.CharField(_('CurrentRatio'), max_length=255, blank=True) # 1.9848232493235696
    InterestCoverageRatio = models.CharField(_('InterestCoverageRatio'), max_length=255, blank=True) # null
    LongtermDebtOverEquity = models.CharField(_('LongtermDebtOverEquity'), max_length=255, blank=True) # null
    TotalDebtOverEquity = models.CharField(_('TotalDebtOverEquity'), max_length=255, blank=True) # 0.5779800665865592
    TotalDebtOverAssets = models.CharField(_('TotalDebtOverAssets'), max_length=255, blank=True) # 0.36627843331179016
    PreTaxMargin = models.CharField(_('PreTaxMargin'), max_length=255, blank=True) # 0.2611064692935692
    NetProfitMargin = models.CharField(_('NetProfitMargin'), max_length=255, blank=True) # 0.05626635339383114
    ROE = models.CharField(_('ROE'), max_length=255, blank=True) # 0.1077439470770574
    ROA = models.CharField(_('ROA'), max_length=255, blank=True) # 0.06293726505582908
    ROIC = models.CharField(_('ROIC'), max_length=255, blank=True) # 0.09799300843651451
    EBIT = models.CharField(_('EBIT'), max_length=255, blank=True) # 39764033130
    EBITDA = models.CharField(_('EBITDA'), max_length=255, blank=True) # 39764033130
    ROCE = models.CharField(_('ROCE'), max_length=255, blank=True) # 0.11821293393856784
    CurrentAssetsTurnover = models.CharField(_('CurrentAssetsTurnover'), max_length=255, blank=True) # 2.178631302206994
    InventoryTurnover = models.CharField(_('InventoryTurnover'), max_length=255, blank=True) # 18.54768501993482
    ReceivablesTurnover = models.CharField(_('ReceivablesTurnover'), max_length=255, blank=True) # 2.322149398043216
    TotalAssetsTurnover = models.CharField(_('TotalAssetsTurnover'), max_length=255, blank=True) # 1.1185595166494178
    ProfitFromFinancialActivitiesOverProfitBeforeTax = models.CharField(_('ProfitFromFinancialActivitiesOverProfitBeforeTax'), max_length=255, blank=True) # -0.05315645312801538
    SalesGrowth_MRQ = models.CharField(_('SalesGrowth_MRQ'), max_length=255, blank=True) # -0.3322128877152136
    SalesGrowth_MRQ2 = models.CharField(_('SalesGrowth_MRQ2'), max_length=255, blank=True) # 0.1401761823532466
    SalesGrowth_TTM = models.CharField(_('SalesGrowth_TTM'), max_length=255, blank=True) # 0.1652608873382776
    SalesGrowth_LFY = models.CharField(_('SalesGrowth_LFY'), max_length=255, blank=True) # 0.16630920913815728
    SalesGrowth_03Yr = models.CharField(_('SalesGrowth_03Yr'), max_length=255, blank=True) # 0.5263809737779408
    ProfitGrowth_MRQ = models.CharField(_('ProfitGrowth_MRQ'), max_length=255, blank=True) # -0.7128508219041308
    ProfitGrowth_MRQ2 = models.CharField(_('ProfitGrowth_MRQ2'), max_length=255, blank=True) # 0.21047857181609667
    ProfitGrowth_TTM = models.CharField(_('ProfitGrowth_TTM'), max_length=255, blank=True) # -0.15660380305905258
    ProfitGrowth_LFY = models.CharField(_('ProfitGrowth_LFY'), max_length=255, blank=True) # -0.16215072736067948
    ProfitGrowth_03Yr = models.CharField(_('ProfitGrowth_03Yr'), max_length=255, blank=True) # 0.3131617805798068
    BasicEPSGrowth_MRQ = models.CharField(_('BasicEPSGrowth_MRQ'), max_length=255, blank=True) # -0.8696098354945888
    BasicEPSGrowth_MRQ2 = models.CharField(_('BasicEPSGrowth_MRQ2'), max_length=255, blank=True) # -0.5475397600446555
    BasicEPSGrowth_TTM = models.CharField(_('BasicEPSGrowth_TTM'), max_length=255, blank=True) # -0.5962029916533123
    BasicEPSGrowth_LFY = models.CharField(_('BasicEPSGrowth_LFY'), max_length=255, blank=True) # -0.5472232456159267
    BasicEPSGrowth_03Yr = models.CharField(_('BasicEPSGrowth_03Yr'), max_length=255, blank=True) # 0.09232815585403054
    DilutedEPSGrowth_MRQ = models.CharField(_('DilutedEPSGrowth_MRQ'), max_length=255, blank=True) # -0.8696098354945888
    DilutedEPSGrowth_MRQ2 = models.CharField(_('DilutedEPSGrowth_MRQ2'), max_length=255, blank=True) # -0.5475397600446555
    DilutedEPSGrowth_TTM = models.CharField(_('DilutedEPSGrowth_TTM'), max_length=255, blank=True) # -0.6181212656133894
    DilutedEPSGrowth_LFY = models.CharField(_('DilutedEPSGrowth_LFY'), max_length=255, blank=True) # -0.6141495390835081
    DilutedEPSGrowth_03Yr = models.CharField(_('DilutedEPSGrowth_03Yr'), max_length=255, blank=True) # 0.09232815585403054
    EquityGrowth_MRQ = models.CharField(_('EquityGrowth_MRQ'), max_length=255, blank=True) # 0.8773983295411654
    EquityGrowth_TTM = models.CharField(_('EquityGrowth_TTM'), max_length=255, blank=True) # 0.8637933359907832
    EquityGrowth_03Yr = models.CharField(_('EquityGrowth_03Yr'), max_length=255, blank=True) # 0.37658549681212716
    TotalAssetsGrowth_MRQ = models.CharField(_('TotalAssetsGrowth_MRQ'), max_length=255, blank=True) # 0.504352510286165
    TotalAssetsGrowth_MRQ2 = models.CharField(_('TotalAssetsGrowth_MRQ2'), max_length=255, blank=True) # 0.39212717609795034
    TotalAssetsGrowth_TTM = models.CharField(_('TotalAssetsGrowth_TTM'), max_length=255, blank=True) # 0.38906418351619093
    TotalAssetsGrowth_LFY = models.CharField(_('TotalAssetsGrowth_LFY'), max_length=255, blank=True) # 0.5089871244021729
    TotalAssetsGrowth_03Yr = models.CharField(_('TotalAssetsGrowth_03Yr'), max_length=255, blank=True) # 0.19993339712796754
    CharterCapitalGrowth_MRQ = models.CharField(_('CharterCapitalGrowth_MRQ'), max_length=255, blank=True) # 1.2173916431002834
    CharterCapitalGrowth_TTM = models.CharField(_('CharterCapitalGrowth_TTM'), max_length=255, blank=True) # 1.1204817827841376
    CharterCapitalGrowth_03Yr = models.CharField(_('CharterCapitalGrowth_03Yr'), max_length=255, blank=True) # 0.45579710770009463
    StockHolderEquityGrowth_MRQ = models.CharField(_('StockHolderEquityGrowth_MRQ'), max_length=255, blank=True) # 0.8773983295411654
    StockHolderEquityGrowth_TTM = models.CharField(_('StockHolderEquityGrowth_TTM'), max_length=255, blank=True) # 0.8637933359907832
    StockHolderEquityGrowth_03Yr = models.CharField(_('StockHolderEquityGrowth_03Yr'), max_length=255, blank=True) # 0.37658549681212716
    EBITMargin_03YrAvg = models.CharField(_('EBITMargin_03YrAvg'), max_length=255, blank=True) # 0.09112913639116545
    GrossMargin_03YrAvg = models.CharField(_('GrossMargin_03YrAvg'), max_length=255, blank=True) # 0.1279655776586451
    NetProfitMargin_03YrAvg = models.CharField(_('NetProfitMargin_03YrAvg'), max_length=255, blank=True) # 0.07119774000102208
    OperatingMargin_03YrAvg = models.CharField(_('OperatingMargin_03YrAvg'), max_length=255, blank=True) # 0.08937224762117163
    PreTaxMargin_03YrAvg = models.CharField(_('PreTaxMargin_03YrAvg'), max_length=255, blank=True) # 0.09112913639116545
    ROA_03YrAvg = models.CharField(_('ROA_03YrAvg'), max_length=255, blank=True) # 0.06891823717388257
    ROE_03YrAvg = models.CharField(_('ROE_03YrAvg'), max_length=255, blank=True) # 0.13385212567118523
    ROIC_03YrAvg = models.CharField(_('ROIC_03YrAvg'), max_length=255, blank=True) # 0.11497170668741018
    DividendInCash_03YrAvg = models.CharField(_('DividendInCash_03YrAvg'), max_length=255, blank=True) # 333.3333333333333
    DividendInShares_03YrAvg = models.CharField(_('DividendInShares_03YrAvg'), max_length=255, blank=True) # 0.049999999999999996
    FreeShares = models.CharField(_('FreeShares'), max_length=255, blank=True) # 17776246
    LastDividendInCash = models.CharField(_('LastDividendInCash'), max_length=255, blank=True) # 1000
    LastDividendInCashRecordDate = models.CharField(_('LastDividendInCashRecordDate'), max_length=255, blank=True) # "2019-06-28T00:00:00"
    NextDividendInCash = models.CharField(_('NextDividendInCash'), max_length=255, blank=True) # null
    NextDividendInCashRecordDate = models.CharField(_('NextDividendInCashRecordDate'), max_length=255, blank=True) # null
    LastDividendInShares = models.CharField(_('LastDividendInShares'), max_length=255, blank=True) # 0.15
    LastDividendInSharesRecordDate = models.CharField(_('LastDividendInSharesRecordDate'), max_length=255, blank=True) # "2018-10-04T00:00:00"
    NextDividendInShares = models.CharField(_('NextDividendInShares'), max_length=255, blank=True) # null
    NextDividendInSharesRecordDate = models.CharField(_('NextDividendInSharesRecordDate'), max_length=255, blank=True) # null
    CashDividend = models.CharField(_('CashDividend'), max_length=255, blank=True) # null
    StockDividend = models.CharField(_('StockDividend'), max_length=255, blank=True) # null
    RetentionRatio = models.CharField(_('RetentionRatio'), max_length=255, blank=True) # null
    DividendYield = models.CharField(_('DividendYield'), max_length=255, blank=True) # null
    TotalStockReturn = models.CharField(_('TotalStockReturn'), max_length=255, blank=True) # null
    CapitalGainsYield = models.CharField(_('CapitalGainsYield'), max_length=255, blank=True) # null
    PayoutRatio = models.CharField(_('PayoutRatio'), max_length=255, blank=True) # null
    LastCashDividendYear = models.CharField(_('LastCashDividendYear'), max_length=255, blank=True) # null
    LastStockDividendYear = models.CharField(_('LastStockDividendYear'), max_length=255, blank=True) # null
    COF = models.CharField(_('COF'), max_length=255, blank=True) # null
    CostToAssets = models.CharField(_('CostToAssets'), max_length=255, blank=True) # null
    CostToIncome = models.CharField(_('CostToIncome'), max_length=255, blank=True) # null
    CostToLoans = models.CharField(_('CostToLoans'), max_length=255, blank=True) # null
    EquityToLoans = models.CharField(_('EquityToLoans'), max_length=255, blank=True) # null
    LAR = models.CharField(_('LAR'), max_length=255, blank=True) # null
    LDR = models.CharField(_('LDR'), max_length=255, blank=True) # null
    LoanlossReservesToLoans = models.CharField(_('LoanlossReservesToLoans'), max_length=255, blank=True) # null
    LoanlossReservesToNPLs = models.CharField(_('LoanlossReservesToNPLs'), max_length=255, blank=True) # null
    LoansToDeposit = models.CharField(_('LoansToDeposit'), max_length=255, blank=True) # null
    NIM = models.CharField(_('NIM'), max_length=255, blank=True) # null
    NonInterestIncomeToNetInterestIncome = models.CharField(_('NonInterestIncomeToNetInterestIncome'), max_length=255, blank=True) # null
    NPLs = models.CharField(_('NPLs'), max_length=255, blank=True) # null
    NPLsToLoans = models.CharField(_('NPLsToLoans'), max_length=255, blank=True) # null
    PreprovisionROA = models.CharField(_('PreprovisionROA'), max_length=255, blank=True) # null
    ProvisionChargesToLoans = models.CharField(_('ProvisionChargesToLoans'), max_length=255, blank=True) # null
    YOEA = models.CharField(_('YOEA'), max_length=255, blank=True) # null
    PC = models.CharField(_('PC'), max_length=255, blank=True) # null
    PT = models.CharField(_('PT'), max_length=255, blank=True) # null
    Cash = models.CharField(_('Cash'), max_length=255, blank=True) # 19757069423
    TotalCurrentAssets = models.CharField(_('TotalCurrentAssets'), max_length=255, blank=True) # 320125945424
    FixedAssets = models.CharField(_('FixedAssets'), max_length=255, blank=True) # 40632023898
    TotalAssets = models.CharField(_('TotalAssets'), max_length=255, blank=True) # 588735324161
    TotalShortTermLiabilities = models.CharField(_('TotalShortTermLiabilities'), max_length=255, blank=True) # 161286878080
    TotalLiabilities = models.CharField(_('TotalLiabilities'), max_length=255, blank=True) # 215641052169
    TotalLongTermLiabilities = models.CharField(_('TotalLongTermLiabilities'), max_length=255, blank=True) # 54354174089
    TotalInventories = models.CharField(_('TotalInventories'), max_length=255, blank=True) # 24245274352
    StockHolderEquity = models.CharField(_('StockHolderEquity'), max_length=255, blank=True) # 373094271992
    GrossProfit = models.CharField(_('GrossProfit'), max_length=255, blank=True) # 13435712711
    ProfitFromFinancialActivities = models.CharField(_('ProfitFromFinancialActivities'), max_length=255, blank=True) # -2106753957
    OtherProfit = models.CharField(_('OtherProfit'), max_length=255, blank=True) # -407831462
    NetSales = models.CharField(_('NetSales'), max_length=255, blank=True) # 547472229156
    ProfitAfterIncomeTaxes = models.CharField(_('ProfitAfterIncomeTaxes'), max_length=255, blank=True) # 30804265919
    ProfitBeforeIncomeTaxes = models.CharField(_('ProfitBeforeIncomeTaxes'), max_length=255, blank=True) # 39633079956

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('LatestFinancialInfo')
        verbosee_name_plural = _('LatestFinancialInfo')

    def __str__(self):
        return 'LatestFinancialInfo-{}-{}'.format(self.Symbol, self.Date)


class IntradayQuote(SoftDeletableModel, TimeStampedModel):
    Symbol = models.CharField(_('Symbol'), max_length=255, blank=True) # "AAV"
    Date = models.CharField(_('Date'), max_length=255, blank=True) # "2020-03-02T02:06:28.88Z"
    Price = models.CharField(_('Price'), max_length=255, blank=True) # 6700
    Volume = models.CharField(_('Volume'), max_length=255, blank=True) # 3400
    TotalVolume = models.CharField(_('TotalVolume'), max_length=255, blank=True) # 12000
    Side = models.CharField(_('Side'), max_length=255, blank=True) # "S"

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('IntradayQuote')
        verbosee_name_plural = _('IntradayQuotes')

    def __str__(self):
        return 'IntradayQuote-{}-{}'.format(self.Symbol, self.Date)


class HistoricalQuote(SoftDeletableModel, TimeStampedModel):
    Symbol = models.CharField(_('Symbol'), max_length=255, blank=True) # "AAV"
    Close = models.CharField(_('Close'), max_length=255, blank=True) # 8600
    Open = models.CharField(_('Open'), max_length=255, blank=True) # 8300
    High = models.CharField(_('High'), max_length=255, blank=True) # 8600
    Low = models.CharField(_('Low'), max_length=255, blank=True) # 8300
    Volume = models.CharField(_('Volume'), max_length=255, blank=True) # 55100
    Value = models.CharField(_('Value'), max_length=255, blank=True) # 0
    Date = models.CharField(_('Date'), max_length=255, blank=True) # "2019-12-03T00:00:00Z"
    OpenInt = models.CharField(_('OpenInt'), max_length=255, blank=True) # 0

    class Meta:
        ordering = ('-created', '-id',)
        verbose_name = _('HistoricalQuote')
        verbosee_name_plural = _('HistoricalQuotes')

    def __str__(self):
        return 'HistoricalQuote-{}-{}'.format(self.Symbol, self.Date)