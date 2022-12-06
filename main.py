#Jayden Lodge Nov 27 2021
#QAP 4




# Reads values in DSICDef.dat

f = open("DSICDef.dat", "r")

PolicyNum = int(f.readline())
BasicPremium = float(f.readline())
DiscountAdditionCar = float(f.readline())
LiabilityCoverage = float(f.readline())
GlassCoverageCost = float(f.readline())
LoanerCarCoverage = float(f.readline())
HSTRate = float(f.readline())
ProcessFeeMonth = float(f.readline())

f.close()

while True:

    #inputs
    CustNameFirst = input("Enter customer first name: ").title()
    CustNameLast = input("Enter customer last name: ").title()
    Address = input("Enter address: ").upper()
    City = input("Enter City: ").title()
    Provence = input("Enter province: ").upper()
    PostalCode = input("Enter postal code: ").upper()
    Phone = input("Enter phone number: ")
    NumCars = int(input("Enter number of cars insured: "))

    ExtraLiability = input("Enter for liability Y/N:").upper()
    if ExtraLiability == "Y":
        ExtraLiability = "YES"
    elif ExtraLiability == "N":
        ExtraLiability = 0

    GlassCoverage = input("Enter if you want glass coverage Y/N: ").upper()

    LoanerCar = input("Enter if your insurance is for a loaner car Y/N: ").upper()
    if LoanerCar == "Y":
        LoanerCar = "YES"
    else:
        LoanerCar = "NO"
    PayOption = input("Enter if customer pays in full or monlthy F/M: ").upper()



    InsurancePremiums = BasicPremium
    if NumCars >= 2:
        InsurancePremiums = (NumCars - 1) * 800 - (BasicPremium * DiscountAdditionCar) + BasicPremium



    Liability = 0
    if LoanerCar == "YES":
        Liability = LiabilityCoverage * NumCars
    elif GlassCoverage == "Y":
        Liability = LiabilityCoverage * NumCars
    elif ExtraLiability == "YES":
        Liability = LiabilityCoverage * NumCars

    if LoanerCar == "YES":
         LoanerCar = LoanerCarCoverage * NumCars

    if GlassCoverage == "Y":
        GlassCoverage = GlassCoverageCost * NumCars
    elif GlassCoverage == "N":
        GlassCoverage = 0
    # cal

    TotalExtraCost = (NumCars * Liability) + GlassCoverageCost + LoanerCarCoverage
    TotalInsurancePremuim = InsurancePremiums + TotalExtraCost
    HST = TotalInsurancePremuim * HSTRate
    TotalCost = TotalInsurancePremuim + HST

    Monthly = (TotalCost / 8) + ProcessFeeMonth
    if PayOption == "M":
        PayOption = Monthly

    #Dsp
    MonthlyDsp = "${:,.2f}".format(Monthly)
    TotalExtraCostDsp = "${:,.2f}".format(TotalExtraCost)
    TotInsurancePremuimDsp = "${:,.2f}".format(TotalInsurancePremuim)
    HSTDsp = "${:,.2f}".format(HST)
    TotalCostDsp = "${:,.2f}".format(TotalCost)
    LiabilityDSP = "${:,.2f}".format(Liability)

    print()
    print()
    print("          One Stop Insurance Company")
    print("_"*40)
    print("Name:", " "*21, f"{CustNameFirst} {CustNameLast} ")
    print(" "*27, f"{Address} ")
    print(" "*27, f"{City}, {Provence}")
    print(" "*27, f"{PostalCode}")
    print("Phone:", " "*19, f" {Phone} ")
    print("_"*40)
    print(f"Loaner car:"," "*14, f" {LoanerCar}")
    print(f"Number of cars insured:", " "*2, f" {NumCars} ")
    print("_"*40)
    if PayOption == Monthly:
        print(f"Monthly Fee:", " "*13, f" {MonthlyDsp}")
        print(f"Processing Fee:", " "*10, f" ${ProcessFeeMonth}")
        print("_"*40)
    print("Extra liability:", " "*9, f" {ExtraLiability} ")
    print("Liability Coverage:", " "*7, f"{LiabilityDSP}")
    print("Glass coverage:", " "*10, f" ${GlassCoverage} ")
    print("_"*40)
    print("Total Extra cost:", " "*8, f" {TotalExtraCostDsp}")
    print("Total insurance Premium:",f"   {TotInsurancePremuimDsp}")
    print("_"*40)
    print("HST:", " "*21, f" {HSTDsp} ")
    print("Total:", " "*19, f" {TotalCostDsp}")
    print("_"*40)
    print()
    print()


    f = open("Policies.dat", "a")

    f.write("{}, ".format(PolicyNum))
    f.write("{}, ".format(CustNameFirst))
    f.write("{}, ".format(CustNameLast))
    f.write("{}, ".format(Address))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Provence))
    f.write("{}, ".format(PostalCode))
    f.write("{}, ".format(Phone))
    f.write("{}, ".format(NumCars))
    f.write("{}, ".format(GlassCoverage))
    f.write("{}, ".format(LoanerCar))
    f.write("{},\n ".format(PayOption))

    PolicyNum += 1
    f.close()


    message = "Policy information processed and saved."
    print(message)



    print("Enter another Insurance plan?")
    QuitOption = input("Type END to quit: ").upper()
    if QuitOption == "END":
        break
