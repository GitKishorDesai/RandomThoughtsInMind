while True:
  #Taking Inputs for Various Income Sources
  print("      INCOMES      ")
  print("Note: Enter the Annual Figures, without Commas and Enter 0 if not applicable")
  ginc=int(input("Enter the Gross Annual Income: "))
  interest=int(input("Enter the Interest earned on Savings Bank Accounts: "))
  othso=int(input("Enter Income from Other Sources(eg:Income on Fixed Deposits): "))
  #Computing Total Income
  totinc=ginc+interest+othso
  print("")
  if totinc==0:
    print(f"Total Income is Rs.{totinc}, hence there will be no Tax Applicable and Total Tax is Rs.0")
    break
  else:
    print(f"Total Income is Rs.{totinc}")

  print("")
  print("")
  print("...........................")
  print("")
  #Taking Input for Various Deductions
  print("      DEDUCTIONS     ")
  print("Maximum/Total Deductions available are: Rs.1,50,000 under Section-80C of Income Tax Act, Rs.50,000 for Contribution in NPS, Rs.10,000 for Interest earned on Savings Bank Accounts")
  print(f"and Rs.50,000 as a Standard Deduction available to everyone")
  print("Note: Enter the Annual Figures, without Commas and Enter 0 if not applicable")
  hra=int(input("Enter the HRA(House Rent Allowance) component of Gross Annual Income: "))
  hins=int(input("Enter the Annual Health Insurance Premium Paid: "))
  lins=int(input("Enter the Annual Life Insurance Premium Paid: "))
  pf=int(input("Enter the Sum of EPF and PPF Contributions for the Year: "))
  tf=int(input("Enter the Annual Tuition Fee Paid for the Child's Education: "))
  od=int(input("Enter the Sum of Investments made in Tax Saving Instruments like ELSS Mutual Fund, Tax Saver FD, etc: "))
  #Computing Deductions under Section-80C
  partded=hins+lins+pf+tf+od
  if partded<150000:
    print(f"Total Deductions under Section-80C = Rs.{partded} and total eligible Deduction for Tax Calculation is Rs.{partded}")
  else:
    print(f"Your Total Deduction under Section-80C is {partded}, but maximum allowed Deduction under Section-80C is Rs.1,50,000, so eligible Deduction for Tax Calculation is Rs.1,50,000")
    partded=150000
  nps=int(input("Enter the Annual NPS Contribution: "))
  if nps!=0:
    if nps<50000:
      print(f"Your Annual NPS Contribution is {nps} and eligible Deduction for Tax Calculation is Rs.{nps}")
      npsded=nps
    else:
      print(f"Your Annual NPS Contribution is {nps}, but maximum allowed Deduction for Tax Calculation is Rs.50,000, hence eligible Deduction for Tax Calculation is Rs.50,000")
      npsded=50000
  else:
    npsded=0
  stded=50000
  if interest!=0:
    if interest<=10000:
      print(f"Interest earned from Savings Bank Accounts is {interest} and eligible Deduction for Tax Calculation is Rs.{interest}")
      intded=interest
    else:
      print(f"Interest earned from Savings Bank Accounts is {interest}, but Maximum allowed Deduction for Tax Calculation is Rs.10,000, hence eligible Deduction for Tax Calculation")
      print(f"is Rs.10,000")
      intded=10000
  else:
    intded=0
    #Computing Total Deductions
  totded=stded+partded+npsded+intded
  print("")
  print(f"Total Deductions available for Tax Calculation is Section-80C Deductions = Rs.{partded} + NPS Deduction = Rs.{npsded} + Standard Deduction = Rs.50,000, which equals")
  print(f"Rs.{totded}")

  print("")
  print("")
  print("...........................")
  print("")
  #Computing Net Taxable Income
  taxinc=totinc-totded
  print(f"Net Taxable Income is Total Income - Total Deductions, which is Rs.{taxinc}")

  print("")
  print("...........................")
  print("")

  #Computing Tax Amount Due based on Net Taxable Income Levels.
  if taxinc<250000:
    print(f"No Income Tax is applicable if Net Taxable Income is Rs.{taxinc}")
    break
  elif 250000<=taxinc<500000:
    tax=(5/100)*taxinc
    print(f"Income Tax for Net Taxable Income of Rs.{taxinc} will be Taxed at 0% for the first 2.5Lakhs and at 5% for the remaining amount, therefore Total Tax equates to Rs.{tax}")
    print(f"But, no need to worry as according to Sec-87A of the Income Tax Act, if Net Taxable Income is below Rs.5Lakh, then one gets a rebate of upto Rs.12,500")
    print(f"Here since the Net Taxable Income is Rs.{taxinc}, you are eligible for the rebate of the Income Tax Amount of Rs.{tax} effectively making your Total Tax as Rs.0")
    break
  elif 500000<=taxinc<1000000:
    tax=12500+((20/100)*(taxinc-500000))
    tax=tax+((4/100)*tax)
    print(f"Income Tax for Net Taxable Income of Rs.{taxinc} will be Taxed at 0% for the first 2.5Lakhs, 5% for next 2.5Lakhs, 20% for the remaining amount and additional 4% Health")
    print(f"and Education Cess, therefore Total Tax equates to Rs.{tax}")
    break
  elif 1000000<=taxinc<5000000:
    tax=112500+((30/100)*(taxinc-1000000))
    tax=tax+((4/100)*(tax))
    print(f"Income Tax for Net Taxable Income of Rs.{taxinc} will be Taxed at 5% for first 5Lakhs, 20% for the next 5Lakhs, 30% for the remaining amount and additonal 4% Health")
    print(f"and Education Cess, therefore Total Tax equates to Rs.{tax}")
    break
  elif 5000000<=taxinc<10000000:
    tax=112500+((30/100)*(taxinc-1000000))
    tax=tax+((4/100)*(tax))+((10/100)*(tax))
    print(f"Income Tax for Net Taxable Income of Rs.{taxinc} will be Taxed at 5% for first 5Lakhs, 20% for the next 5Lakhs, 30% for the remaining amount, 4% Health and Education Cess")
    print(f"and additional 10% surcharge, therefore Total Tax equates to Rs.{tax}")
    break
  elif 10000000<=taxinc:
    tax=112500+((30/100)*(taxinc-1000000))
    tax=tax+((4/100)*tax)+((20/100)*tax)
    print(f"Income Tax for Net Taxable Income of Rs.{taxinc} will be Taxed at 5% for first 5Lakhs, 20% for the next 5Lakhs, 30% for the remaining amount, 4% Health and Education Cess")
    print(f"and additional 20% surcharge, therefore Total Tax equates to Rs.{tax}")
    break
    
