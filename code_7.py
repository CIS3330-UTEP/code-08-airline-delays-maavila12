import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns 
import statsmodels.api as sm 
import statsmodels.formula.api as smf 
#If any of this libraries is missing from your computer. Please install them using pip.


# descriptive analytics
filename = 'Flight_Delays_2018.csv'

df= pd.read_csv(filename)
# outliers
df.boxplot(column = 'ARR_DELAY', by = 'OP_CARRIER_NAME')
plt.xticks(rotation=90) 
plt.show()
print(df.groupby('OP_CARRIER_NAME')['ARR_DELAY'].agg('mean', 'median'))
#correlationof prediuctor variables with dependent variable (ARR_DELAY)
corr_matrix = df.corr(numeric_only=True) # to get correlation matrix for numeric columns only.      This line was generated by copilot thru Visual Studio Code.
corr_matrix = corr_matrix.round(2)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmax=1, vmin=-1)


#descriptive Analytics

airlines = ['American Airlines INC.', 'Endeavor Air Inc', 'Delta Air Lines Inc.', 'Republic Airlines']
df = df.query("OP_CARRIER_NAME == @airlines") 

model = smf.ols('ARR_DELAY ~ (DEP_DELAY)', data=df).fit() #The last part of the line was generated by Copilot on Visual Studio Code.
print(model.summary())
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

#scatterplotwith regression line
sns.lmplot(x='DEP_DELAY', y='ARR_DELAY', data=df, line_kws={'color': 'red'})
plt.title('Scatterplot of Arrival Delay vs Departure Delay')
plt.xlabel('Departure Delay (minutes)')
plt.ylabel('Arrival Delay (minutes)')
plt.show()