import scipy.stats as stats
import pandas as pd

df = pd.read_csv('day.csv') 


groups = [df[df['season'] == s]['cnt'] for s in df['season'].unique()]
f_val, p_val = stats.f_oneway(*groups)
print("ANOVA F=", f_val, ", p=", p_val)

# Kruskal-Wallis
kw_stat, kw_p = stats.kruskal(*groups)
print("Kruskal-Wallis H=", kw_stat, ", p=", kw_p)
