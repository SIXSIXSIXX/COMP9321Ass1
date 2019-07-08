import pandas as pd
import matplotlib.pyplot as plot
import re

"""Write with python 3.5.1"""
def merge_dfs(df1, df2):
    """merge two dfs"""
    return pd.merge(df1, df2, how='left', left_on='Country', right_on='Country')


def print_line():
    """print separate line"""
    print('---------------------------------------------------------------------------------------------------------')


def question_1(df):
    print('Question 1:\n')
    for index, row in df.head(5).iterrows():
        for column in df:
            print(",".join([str(row[column])]))

    print_line()


def question_2(df):
    print('\nQuestion 2:\n')
    print(df.head(1))
    print_line()


def question_3(df):
    print('\nQuestion 3:\n')
    print(df.head(5))
    print_line()


def question_4(df):
    print('\nQuestion 4:\n')
    print(df.tail(10))
    print_line()


def question_5(df):
    print('\nQuestion 5:\n')
    df = df.sort_values(by=['Summer_Gold'],ascending=False)
    print(df.iloc[[1]]['Country'].to_string(index=False)+' The number of Gold medals in summer games are '+df.iloc[[1]]['Summer_Gold'].to_string(index=False))
    print_line()


def question_6(df):
    print('\nQuestion 6:\n')
    df['diff'] = abs(df['Summer_Gold']-df['Winter_Gold'])
    df = df.sort_values(by=['diff'], ascending=False)
    print(df.iloc[[1]]['Country'].to_string(index=False)+' The difference is: '+df.iloc[[1]]['diff'].to_string(index=False))
    print_line()


def question_7(df):
    print('\nQuestion 7:\n')
    df= df.sort_values(by=['All_Total'],ascending=False)
    print('First five rows')
    print(df.head(5))
    print('')
    print('Last five rows')
    print(df.tail(5))
    print_line()
    return df


def question_8(df):
    print('\nQuestion 8:\n')
    head_10 = df.iloc[1:11]
    df['Country']= [re.sub(r'\(.+', '', value) for value in df['Country']]
    head_10=head_10.set_index('Country', drop=True)
    head_10[['Summer_Total','Winter_Total']].plot.barh(stacked=True);
    plot.xlabel('Total Medal', fontsize=12)
    plot.ylabel('Country', fontsize=12)
    plot.title('Medals for Winter and Summer Games',fontsize=12)
    plot.tight_layout()
    plot.show()
    print_line()


def question_9(df):
    print('\nQuestion 9:\n')
    # df = df.set_index('Country',drop=True)
    USA = df.Country.str.contains('United States')
    ANZ = df.Country.str.contains('Australia')
    Britain = df.Country.str.contains('Great Britain')
    Jap = df.Country.str.contains('Japan')
    NZ = df.Country.str.contains('New Zealand')
    five_cty = df[USA|ANZ|Britain|Jap|NZ]
    five_cty['Country'] = [re.sub(r' \(.+','', value) for value in five_cty['Country']]
    five_cty = five_cty.set_index('Country',drop=True)
    five_cty[['Winter_Gold','Winter_Silver','Winter_Bronze']].plot.bar(rot=0)
    plot.xlabel('Country',fontsize=12)
    plot.ylabel('Medals number',fontsize=12)
    plot.title('Medals for Winter Games',fontsize=12)
    plot.legend(['Gold','Silver','Bronze'])
    plot.tight_layout()
    plot.show()
    print_line()


if __name__ == "__main__":
    """20 columns are enough"""
    pd.set_option('display.max_columns', 20)
    """Magic number"""
    pd.set_option('display.width',1000)
    pd.options.mode.chained_assignment = None
    csv1 = 'Olympics_dataset1.csv'
    csv2 = 'Olympics_dataset2.csv'
    olyp1 = pd.read_csv(csv1,thousands=",",skiprows=1)
    olyp1.columns = ['Country','Rubbish','Summer_games','Summer_Gold','Summer_Silver','Summer_Bronze','Summer_Total']
    olyp2 = pd.read_csv(csv2,thousands=",",skiprows=1)
    olyp2.columns = ['Country', 'Winter_games', 'Winter_Gold', 'Winter_Silver', 'Winter_Bronze', 'Winter_Total',
                     'Combine_Games', 'Total_Gold', 'Total_Silver', 'Total_Bronze', 'All_Total']
    merge_olyp = merge_dfs(olyp1,olyp2)
    question_1(merge_olyp)
    # """set the country as index"""
    # country_index=merge_olyp.set_index('Country', drop=True)
    # question_2(country_index)
    # """drop rubbish column of df"""
    # df_noRubbish = merge_olyp.drop(columns=['Rubbish'])
    # question_3(df_noRubbish)
    # """Drop NAN value row"""
    # df_noNaN = merge_olyp.dropna()
    # question_4(df_noNaN)
    # question_5(merge_olyp)
    # question_6(merge_olyp)
    # df_q7 = question_7(merge_olyp)
    # question_8(df_q7)
    # question_9(merge_olyp)
