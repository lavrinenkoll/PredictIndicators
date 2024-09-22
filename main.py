import pandas
from scipy.interpolate import make_interp_spline
import numpy


def parsing():

    # Read the data from the file, 1st sheet
    data = pandas.read_excel('Data_Set_14.xlsx', sheet_name='1 Type of sale').T

    # Mortgage sales
    Mortgage_sales = {}

    # Number of sales by sales channel
    Number_of_sales_direct = {}
    Number_of_sales_inter = {}

    # Number of sales by advice given
    Number_of_sales_advice = {}
    Number_of_sales_advice_nonadv = {}

    for i in range(len(data[5][12:])):
        Mortgage_sales[data[5][12:][i]] = data[8][i+12]

        Number_of_sales_direct[data[5][12:][i]] = data[14][i+12]
        Number_of_sales_inter[data[5][12:][i]] = data[15][i+12]

        Number_of_sales_advice[data[5][12:][i]] = data[22][i+12]
        Number_of_sales_advice_nonadv[data[5][12:][i]] = data[23][i+12]

    mortgage = {}
    mortgage['Mortgage sales'] = Mortgage_sales

    sales = {}
    sales['Direct'] = Number_of_sales_direct
    sales['Intermediary'] = Number_of_sales_inter

    advice = {}
    advice['Advised sale'] = Number_of_sales_advice
    advice['Non-advised sale'] = Number_of_sales_advice_nonadv

    # Read the data from the file, 2nd sheet
    data = pandas.read_excel('Data_Set_14.xlsx', sheet_name='2 Loan purpose').T

    council = {}
    first_time = {}
    home_movers = {}
    remortgagors = {}
    not_known = {}
    other = {}

    extra_debt = {}
    extra_home = {}
    extra_home_home_dept = {}
    no_extra = {}
    other2 = {}

    for i in range(len(data[5][12:])):
        council[data[5][12:][i]] = data[8][i+12]
        first_time[data[5][12:][i]] = data[9][i+12]
        home_movers[data[5][12:][i]] = data[10][i+12]
        remortgagors[data[5][12:][i]] = data[11][i+12]
        not_known[data[5][12:][i]] = data[12][i+12]
        other[data[5][12:][i]] = data[13][i+12]

        extra_debt[data[5][12:][i]] = data[20][i+12]
        extra_home[data[5][12:][i]] = data[21][i+12]
        extra_home_home_dept[data[5][12:][i]] = data[22][i+12]
        no_extra[data[5][12:][i]] = data[23][i+12]
        other2[data[5][12:][i]] = data[24][i+12]

    loan_purpose = {}
    loan_purpose['Council/Registered Social Landlord Tenant Exercising Their Right To Buy'] = council
    loan_purpose['First Time Buyer'] = first_time
    loan_purpose['Home Movers (2nd Or Subsequent Buyers)'] = home_movers
    loan_purpose['Remortgagors'] = remortgagors
    loan_purpose['Not Known'] = not_known
    loan_purpose['Other'] = other

    remortgages = {}
    remortgages['Extra money raised for debt consolidation'] = extra_debt
    remortgages['Extra money raised for home improvements'] = extra_home
    remortgages['Extra money raised for home improvements and debt consolidation'] = extra_home_home_dept
    remortgages['No extra money raised'] = no_extra
    remortgages['Other'] = other2

    data = pandas.read_excel('Data_Set_14.xlsx', sheet_name='3 Loan characteristics').T

    price0_50 = {}
    price50_120 = {}
    price120_250 = {}
    price250_500 = {}
    price500 = {}

    capped = {}
    discounted = {}
    fixed = {}
    standard = {}
    tracker = {}
    other = {}

    capital = {}
    endowment = {}
    isa = {}
    pension = {}
    unknown = {}
    mix = {}
    unknown_repayment = {}

    ltv0_30 = {}
    ltv30_50 = {}
    ltv50_75 = {}
    ltv75_85 = {}
    ltv85_90 = {}
    ltv90_95 = {}
    ltv95_100 = {}
    ltv100 = {}

    income_not_verified = {}
    income_verified = {}

    income_joint = {}
    income_sole = {}
    income_unknown = {}

    income_single_2_5 = {}
    income_single_2_5_3_49 = {}
    income_single_3_5_4_49 = {}
    income_single_4_5_5_49 = {}
    income_single_5_5 = {}

    income_joint_2_5 = {}
    income_joint_2_5_3_49 = {}
    income_joint_3_5_4_49 = {}
    income_joint_4_5_5_49 = {}
    income_joint_5_5 = {}

    lifetime = {}
    non_lifetime = {}


    for i in range(len(data[5][12:])):
        price0_50[data[5][12:][i]] = data[8][i+12]
        price50_120[data[5][12:][i]] = data[9][i+12]
        price120_250[data[5][12:][i]] = data[10][i+12]
        price250_500[data[5][12:][i]] = data[11][i+12]
        price500[data[5][12:][i]] = data[12][i+12]

        capped[data[5][12:][i]] = data[19][i+12]
        discounted[data[5][12:][i]] = data[20][i+12]
        fixed[data[5][12:][i]] = data[21][i+12]
        standard[data[5][12:][i]] = data[22][i+12]
        tracker[data[5][12:][i]] = data[23][i+12]
        other[data[5][12:][i]] = data[24][i+12]

        capital[data[5][12:][i]] = data[31][i+12]
        endowment[data[5][12:][i]] = data[32][i+12]
        isa[data[5][12:][i]] = data[33][i+12]
        pension[data[5][12:][i]] = data[34][i+12]
        unknown[data[5][12:][i]] = data[35][i+12]
        mix[data[5][12:][i]] = data[36][i+12]
        unknown_repayment[data[5][12:][i]] = data[37][i+12]

        ltv0_30[data[5][12:][i]] = data[44][i+12]
        ltv30_50[data[5][12:][i]] = data[45][i+12]
        ltv50_75[data[5][12:][i]] = data[46][i+12]
        ltv75_85[data[5][12:][i]] = data[47][i+12]
        ltv85_90[data[5][12:][i]] = data[48][i+12]
        ltv90_95[data[5][12:][i]] = data[49][i+12]
        ltv95_100[data[5][12:][i]] = data[50][i+12]
        ltv100[data[5][12:][i]] = data[51][i+12]

        income_not_verified[data[5][12:][i]] = data[57][i+12]
        income_verified[data[5][12:][i]] = data[58][i+12]

        income_joint[data[5][12:][i]] = data[65][i+12]
        income_sole[data[5][12:][i]] = data[66][i+12]
        income_unknown[data[5][12:][i]] = data[67][i+12]

        income_single_2_5[data[5][12:][i]] = data[74][i+12]
        income_single_2_5_3_49[data[5][12:][i]] = data[75][i+12]
        income_single_3_5_4_49[data[5][12:][i]] = data[76][i+12]
        income_single_4_5_5_49[data[5][12:][i]] = data[77][i+12]
        income_single_5_5[data[5][12:][i]] = data[78][i+12]

        income_joint_2_5[data[5][12:][i]] = data[85][i+12]
        income_joint_2_5_3_49[data[5][12:][i]] = data[86][i+12]
        income_joint_3_5_4_49[data[5][12:][i]] = data[87][i+12]
        income_joint_4_5_5_49[data[5][12:][i]] = data[88][i+12]
        income_joint_5_5[data[5][12:][i]] = data[89][i+12]

        lifetime[data[5][12:][i]] = data[96][i+12]
        non_lifetime[data[5][12:][i]] = data[97][i+12]

    sales_by_loan_amount = {}
    sales_by_loan_amount['£0K - £50K'] = price0_50
    sales_by_loan_amount['£50K - £120K'] = price50_120
    sales_by_loan_amount['£120K - £250K'] = price120_250
    sales_by_loan_amount['£250K - £500K'] = price250_500
    sales_by_loan_amount['£500K +'] = price500

    sales_by_interest_rate_type = {}
    sales_by_interest_rate_type['Capped rate'] = capped
    sales_by_interest_rate_type['Discounted rate'] = discounted
    sales_by_interest_rate_type['Fixed rate'] = fixed
    sales_by_interest_rate_type['Standard variable rate'] = standard
    sales_by_interest_rate_type['Tracker rate'] = tracker
    sales_by_interest_rate_type['Other'] = other

    sales_by_repayment_method = {}
    sales_by_repayment_method['Capital and interest'] = capital
    sales_by_repayment_method['Endowment'] = endowment
    sales_by_repayment_method['ISA'] = isa
    sales_by_repayment_method['Pension'] = pension
    sales_by_repayment_method['Unknown'] = unknown
    sales_by_repayment_method['Mix'] = mix
    sales_by_repayment_method['Unknown repayment method'] = unknown_repayment

    sales_by_LTV_ratio = {}
    sales_by_LTV_ratio['0% - 30%'] = ltv0_30
    sales_by_LTV_ratio['30% - 50%'] = ltv30_50
    sales_by_LTV_ratio['50% - 75%'] = ltv50_75
    sales_by_LTV_ratio['75% - 85%'] = ltv75_85
    sales_by_LTV_ratio['85% - 90%'] = ltv85_90
    sales_by_LTV_ratio['90% - 95%'] = ltv90_95
    sales_by_LTV_ratio['95% - 100%'] = ltv95_100
    sales_by_LTV_ratio['100%'] = ltv100

    sales_by_income_verification = {}
    sales_by_income_verification['Income not verified'] = income_not_verified
    sales_by_income_verification['Income verified'] = income_verified

    sales_by_income_basis = {}
    sales_by_income_basis['Joint'] = income_joint
    sales_by_income_basis['Sole'] = income_sole
    sales_by_income_basis['Unknown'] = income_unknown

    sales_by_income_multipliers_single = {}
    sales_by_income_multipliers_single['<2.5'] = income_single_2_5
    sales_by_income_multipliers_single['2.5 - 3.49'] = income_single_2_5_3_49
    sales_by_income_multipliers_single['3.5 - 4.49'] = income_single_3_5_4_49
    sales_by_income_multipliers_single['4.5 - 5.49'] = income_single_4_5_5_49
    sales_by_income_multipliers_single['>5.5'] = income_single_5_5

    sales_by_income_multipliers_joint = {}
    sales_by_income_multipliers_joint['<2.5'] = income_joint_2_5
    sales_by_income_multipliers_joint['2.5 - 3.49'] = income_joint_2_5_3_49
    sales_by_income_multipliers_joint['3.5 - 4.49'] = income_joint_3_5_4_49
    sales_by_income_multipliers_joint['4.5 - 5.49'] = income_joint_4_5_5_49
    sales_by_income_multipliers_joint['>5.5'] = income_joint_5_5

    sales_by_lifetime = {}
    sales_by_lifetime['Lifetime'] = lifetime
    sales_by_lifetime['Non-lifetime'] = non_lifetime

    data = pandas.read_excel('Data_Set_14.xlsx', sheet_name='4 Borrower characteristics').T

    advanced_impaired = {}
    advanced_not_impaired = {}

    employed = {}
    retired = {}
    self_employed = {}
    other = {}

    age0_20 = {}
    age21_40 = {}
    age41_55 = {}
    age56_65 = {}
    age66_75 = {}
    age76 = {}

    for i in range(0, 12):
        advanced_impaired[data[5][12:][i]] = data[8][i+12]
        advanced_not_impaired[data[5][12:][i]] = data[9][i+12]

        employed[data[5][12:][i]] = data[16][i+12]
        retired[data[5][12:][i]] = data[17][i+12]
        self_employed[data[5][12:][i]] = data[18][i+12]
        other[data[5][12:][i]] = data[19][i+12]

        age0_20[data[5][12:][i]] = data[26][i+12]
        age21_40[data[5][12:][i]] = data[27][i+12]
        age41_55[data[5][12:][i]] = data[28][i+12]
        age56_65[data[5][12:][i]] = data[29][i+12]
        age66_75[data[5][12:][i]] = data[30][i+12]
        age76[data[5][12:][i]] = data[31][i+12]

    number_of_sales_by_credit_history = {}
    number_of_sales_by_credit_history['Mortgages advanced to people with an impaired credit history'] = advanced_impaired
    number_of_sales_by_credit_history['Mortgages advanced to people without an impaired credit history'] = advanced_not_impaired

    number_of_sales_by_employment_status = {}
    number_of_sales_by_employment_status['Employed'] = employed
    number_of_sales_by_employment_status['Retired'] = retired
    number_of_sales_by_employment_status['Self-employed'] = self_employed
    number_of_sales_by_employment_status['Other'] = other

    number_of_sales_by_customer_age_bands = {}
    number_of_sales_by_customer_age_bands['0 - 20'] = age0_20
    number_of_sales_by_customer_age_bands['21 - 40'] = age21_40
    number_of_sales_by_customer_age_bands['41 - 55'] = age41_55
    number_of_sales_by_customer_age_bands['56 - 65'] = age56_65
    number_of_sales_by_customer_age_bands['66 - 75'] = age66_75
    number_of_sales_by_customer_age_bands['76 +'] = age76

    data = pandas.read_excel('Data_Set_14.xlsx', sheet_name='5 Property characteristics').T

    property_value_0_60 = {}
    property_value_60_120 = {}
    property_value_120_250 = {}
    property_value_250_500 = {}
    property_value_500_750 = {}
    property_value_750_1 = {}
    property_value_1 = {}
    property_value_unknown = {}

    region_central = {}
    region_east_midlands = {}
    region_eastern = {}
    region_north_east = {}
    region_north_west = {}
    region_northern_ireland = {}
    region_scotland = {}
    region_south_east = {}
    region_south_west = {}
    region_wales = {}
    region_west_midlands = {}
    region_yorkshire = {}
    region_no_postcode = {}

    for i in range(0, 12):
        property_value_0_60[data[5][12:][i]] = data[8][i+12]
        property_value_60_120[data[5][12:][i]] = data[9][i+12]
        property_value_120_250[data[5][12:][i]] = data[10][i+12]
        property_value_250_500[data[5][12:][i]] = data[11][i+12]
        property_value_500_750[data[5][12:][i]] = data[12][i+12]
        property_value_750_1[data[5][12:][i]] = data[13][i+12]
        property_value_1[data[5][12:][i]] = data[14][i+12]
        property_value_unknown[data[5][12:][i]] = data[15][i+12]

        region_central[data[5][12:][i]] = data[22][i+12]
        region_east_midlands[data[5][12:][i]] = data[23][i+12]
        region_eastern[data[5][12:][i]] = data[24][i+12]
        region_north_east[data[5][12:][i]] = data[25][i+12]
        region_north_west[data[5][12:][i]] = data[26][i+12]
        region_northern_ireland[data[5][12:][i]] = data[27][i+12]
        region_scotland[data[5][12:][i]] = data[28][i+12]
        region_south_east[data[5][12:][i]] = data[29][i+12]
        region_south_west[data[5][12:][i]] = data[30][i+12]
        region_wales[data[5][12:][i]] = data[31][i+12]
        region_west_midlands[data[5][12:][i]] = data[32][i+12]
        region_yorkshire[data[5][12:][i]] = data[33][i+12]
        region_no_postcode[data[5][12:][i]] = data[34][i+12]

    number_of_sales_by_property_value_bands = {}
    number_of_sales_by_property_value_bands['£0K - £60K'] = property_value_0_60
    number_of_sales_by_property_value_bands['£60K - £120K'] = property_value_60_120
    number_of_sales_by_property_value_bands['£120K - £250K'] = property_value_120_250
    number_of_sales_by_property_value_bands['£250K - £500K'] = property_value_250_500
    number_of_sales_by_property_value_bands['£500K - £750K'] = property_value_500_750
    number_of_sales_by_property_value_bands['£750K - £1M'] = property_value_750_1
    number_of_sales_by_property_value_bands['£1M +'] = property_value_1
    number_of_sales_by_property_value_bands['Unknown value'] = property_value_unknown

    number_of_sales_by_region = {}
    number_of_sales_by_region['Central & Greater London'] = region_central
    number_of_sales_by_region['East Midlands'] = region_east_midlands
    number_of_sales_by_region['Eastern'] = region_eastern
    number_of_sales_by_region['North East'] = region_north_east
    number_of_sales_by_region['North West'] = region_north_west
    number_of_sales_by_region['Northern Ireland'] = region_northern_ireland
    number_of_sales_by_region['Scotland'] = region_scotland
    number_of_sales_by_region['South East'] = region_south_east
    number_of_sales_by_region['South West'] = region_south_west
    number_of_sales_by_region['Wales'] = region_wales
    number_of_sales_by_region['West Midlands'] = region_west_midlands
    number_of_sales_by_region['Yorkshire and The Humber'] = region_yorkshire
    number_of_sales_by_region['No postcode'] = region_no_postcode

    data = pandas.read_excel('Data_Set_14.xlsx', sheet_name='6 First-time buyers').T

    single_income_0_25 = {}
    single_income_25_35 = {}
    single_income_35_45 = {}
    single_income_45_55 = {}
    single_income_55 = {}

    joint_income_0_25 = {}
    joint_income_25_35 = {}
    joint_income_35_45 = {}
    joint_income_45_55 = {}
    joint_income_55 = {}

    ltv_0_30 = {}
    ltv_30_50 = {}
    ltv_50_75 = {}
    ltv_75_85 = {}
    ltv_85_90 = {}
    ltv_90_95 = {}
    ltv_95_100 = {}
    ltv_100 = {}

    property_value_0_60 = {}
    property_value_60_120 = {}
    property_value_120_250 = {}
    property_value_250_500 = {}
    property_value_500_750 = {}
    property_value_750_1 = {}
    property_value_1 = {}
    property_value_unknown = {}

    for i in range(len(data[0][12:])):
        single_income_0_25[data[5][12:][i]] = data[8][i+12]
        single_income_25_35[data[5][12:][i]] = data[9][i+12]
        single_income_35_45[data[5][12:][i]] = data[10][i+12]
        single_income_45_55[data[5][12:][i]] = data[11][i+12]
        single_income_55[data[5][12:][i]] = data[12][i+12]

        joint_income_0_25[data[5][12:][i]] = data[19][i+12]
        joint_income_25_35[data[5][12:][i]] = data[20][i+12]
        joint_income_35_45[data[5][12:][i]] = data[21][i+12]
        joint_income_45_55[data[5][12:][i]] = data[22][i+12]
        joint_income_55[data[5][12:][i]] = data[23][i+12]

        ltv_0_30[data[5][12:][i]] = data[30][i+12]
        ltv_30_50[data[5][12:][i]] = data[31][i+12]
        ltv_50_75[data[5][12:][i]] = data[32][i+12]
        ltv_75_85[data[5][12:][i]] = data[33][i+12]
        ltv_85_90[data[5][12:][i]] = data[34][i+12]
        ltv_90_95[data[5][12:][i]] = data[35][i+12]
        ltv_95_100[data[5][12:][i]] = data[36][i+12]
        ltv_100[data[5][12:][i]] = data[37][i+12]

        property_value_0_60[data[5][12:][i]] = data[44][i+12]
        property_value_60_120[data[5][12:][i]] = data[45][i+12]
        property_value_120_250[data[5][12:][i]] = data[46][i+12]
        property_value_250_500[data[5][12:][i]] = data[47][i+12]
        property_value_500_750[data[5][12:][i]] = data[48][i+12]
        property_value_750_1[data[5][12:][i]] = data[49][i+12]
        property_value_1[data[5][12:][i]] = data[50][i+12]
        property_value_unknown[data[5][12:][i]] = data[51][i+12]

    number_of_sales_by_income = {}
    number_of_sales_by_income['< 2.5'] = single_income_0_25
    number_of_sales_by_income['2.5 to 3.49'] = single_income_25_35
    number_of_sales_by_income['3.5 to 4.49'] = single_income_35_45
    number_of_sales_by_income['4.5 to 5.49'] = single_income_45_55
    number_of_sales_by_income['>5.5'] = single_income_55

    number_of_sales_by_joint_income = {}
    number_of_sales_by_joint_income['< 2.5'] = joint_income_0_25
    number_of_sales_by_joint_income['2.5 to 3.49'] = joint_income_25_35
    number_of_sales_by_joint_income['3.5 to 4.49'] = joint_income_35_45
    number_of_sales_by_joint_income['4.5 to 5.49'] = joint_income_45_55
    number_of_sales_by_joint_income['>5.5'] = joint_income_55

    number_of_sales_by_ltv = {}
    number_of_sales_by_ltv['0% - 30%'] = ltv_0_30
    number_of_sales_by_ltv['30% - 50%'] = ltv_30_50
    number_of_sales_by_ltv['50% - 75%'] = ltv_50_75
    number_of_sales_by_ltv['75% - 85%'] = ltv_75_85
    number_of_sales_by_ltv['85% - 90%'] = ltv_85_90
    number_of_sales_by_ltv['90% - 95%'] = ltv_90_95
    number_of_sales_by_ltv['95% - 100%'] = ltv_95_100
    number_of_sales_by_ltv['100%'] = ltv_100

    number_of_sales_by_property_value = {}
    number_of_sales_by_property_value['£0K - £60K'] = property_value_0_60
    number_of_sales_by_property_value['60K - £120K'] = property_value_60_120
    number_of_sales_by_property_value['120K - £250K'] = property_value_120_250
    number_of_sales_by_property_value['250K - £500K'] = property_value_250_500
    number_of_sales_by_property_value['500K - £750K'] = property_value_500_750
    number_of_sales_by_property_value['750K - £1M'] = property_value_750_1
    number_of_sales_by_property_value['> £1M'] = property_value_1
    number_of_sales_by_property_value['Unknown'] = property_value_unknown

    return mortgage, sales, advice,\
               loan_purpose, remortgages, \
        sales_by_loan_amount, sales_by_interest_rate_type, sales_by_repayment_method, sales_by_LTV_ratio, \
        sales_by_income_verification, sales_by_income_basis, sales_by_income_multipliers_single, sales_by_income_multipliers_joint, \
        sales_by_lifetime,\
        number_of_sales_by_credit_history, number_of_sales_by_employment_status, number_of_sales_by_customer_age_bands,\
        number_of_sales_by_property_value_bands, number_of_sales_by_region, \
        number_of_sales_by_income, number_of_sales_by_joint_income, number_of_sales_by_ltv, number_of_sales_by_property_value

#prediction for the next 4 , keras
def prediction(data):

    import numpy as np
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.layers import LSTM

    data = list(data.values())

    x = [i for i in range(len(data))]
    y = data

    x = np.array(x)
    y = np.array(y)

    x = x.reshape((len(x), 1, 1))
    y = y.reshape((len(y), 1))

    #next 4 prediction, keras, small dataset
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(1, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(x, y, epochs=10000, verbose=0)

    x = [i for i in range(len(data), len(data) + 4)]
    x = np.array(x)
    x = x.reshape((len(x), 1, 1))

    y = model.predict(x, verbose=0)
    y = [i[0] for i in y]

    print('Спрогнозовані дані на наступні 4 кваартали:')
    print("2014-Q2: ", y[0])
    print("2014-Q3: ", y[1])
    print("2014-Q4: ", y[2])
    print("2015-Q1: ", y[3])
    data = y
    print("Статичтичні характеристики спрогнозованих даних на наступні 4 квартали")
    print("Очікуване значення: ", numpy.median(data))
    print("Дисперсія: ", numpy.var(data))
    print("Середньоквадратичне відхилення: ", numpy.std(data))
    print("Математичне очікування: ", numpy.mean(data))

    return y

# апроксимация данных
def graph_trend(values, title):
    import matplotlib.pyplot as plt

    predicted = prediction(values)

    values['2014-Q2'] = predicted[0]
    values['2014-Q3'] = predicted[1]
    values['2014-Q4'] = predicted[2]
    values['2015-Q1'] = predicted[3]

    # Plot the total data
    plt.plot(values.keys(), values.values(), label = 'Total')
    plt.xticks(rotation=90, fontsize=6)
    plt.axvline(x='2014-Q1', color='r', linestyle='--')
    plt.title(title+' predicted')

    #smoothing the MNC graph
    x = range(len(values.keys()))
    y = numpy.array(list(values.values()))

    xnew = numpy.linspace(min(x), max(x), 7)
    spl = make_interp_spline(x, y, k=7)
    power_smooth = spl(xnew)
    plt.plot(xnew, power_smooth, label='Trend')
    plt.legend()
    plt.show()

    #bar chart values
    plt.bar(values.keys(), values.values())
    plt.xticks(rotation=90, fontsize=6)
    plt.axvline(x='2014-Q1', color='r', linestyle='--')
    plt.title(title+' predicted')
    plt.show()


def graphing(data, title, prediction_needed):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas

    for key, value in data.items():
        value_temp = {}
        for key2, value2 in value.items():
            if str(value2) != 'nan':
                value_temp[key2] = value2
        data[key] = value_temp

    datagraph = pandas.DataFrame(data)

    # Plot the data
    datagraph.plot(kind='bar', stacked=True, figsize=(10, 5))
    plt.title(title)
    plt.show()

    if prediction_needed:
        values = {}
        for key in data:
            for i in data[key]:
                if i in values:
                    values[i] += data[key][i]
                else:
                    values[i] = data[key][i]

        #plot trend
        graph_trend(values, title)


mortgage, sales, advice, loan_purpose, remortgages, \
sales_by_loan_amount, sales_by_interest_rate_type, sales_by_repayment_method, sales_by_LTV_ratio, \
sales_by_income_verification, sales_by_income_basis, sales_by_income_multipliers_single, sales_by_income_multipliers_joint, \
sales_by_lifetime,\
number_of_sales_by_credit_history, number_of_sales_by_employment_status, number_of_sales_by_customer_age_bands,\
number_of_sales_by_property_value_bands, number_of_sales_by_region, \
number_of_sales_by_income, number_of_sales_by_joint_income, number_of_sales_by_ltv, number_of_sales_by_property_value = parsing()

graphing(mortgage, 'Mortgage sales', True)
graphing(sales, 'Number of sales by sales channel', False)
graphing(advice, 'Number of sales by advice given', False)
graphing(loan_purpose, 'Loan purpose', False)
graphing(remortgages, 'Remortgages', False)
graphing(sales_by_loan_amount, 'Sales by loan amount', False)
graphing(sales_by_interest_rate_type, 'Sales by interest rate type', False)
graphing(sales_by_repayment_method, 'Sales by repayment method', False)
graphing(sales_by_LTV_ratio, 'Sales by LTV ratio', False)
graphing(sales_by_income_verification, 'Sales by income verification', False)
graphing(sales_by_income_basis, 'Sales by income basis', False)
graphing(sales_by_income_multipliers_single, 'Sales by income multipliers single', False)
graphing(sales_by_income_multipliers_joint, 'Sales by income multipliers joint', False)
graphing(sales_by_lifetime, 'Sales by lifetime', False)
graphing(number_of_sales_by_credit_history, 'Number of sales by credit history', False)
graphing(number_of_sales_by_employment_status, 'Number of sales by employment status', False)
graphing(number_of_sales_by_customer_age_bands, 'Number of sales by customer age bands', False)
graphing(number_of_sales_by_property_value_bands, 'Number of sales by property value bands', False)
graphing(number_of_sales_by_region, 'Number of sales by region', False)
graphing(number_of_sales_by_income, 'Number of sales by income', False)
graphing(number_of_sales_by_joint_income, 'Number of sales by joint income', False)
graphing(number_of_sales_by_ltv, 'Number of sales by ltv', False)
graphing(number_of_sales_by_property_value, 'Number of sales by property value', False)