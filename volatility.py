from init import *
from geochart import *

volatilities = []

min = 99999999
max = 0

# for country, df in pd_data.split('country_name').items():
#   volatility = df.sum_of_difference('price_usd') / len(df)
#   if not np.isnan(volatility):
#     if volatility > max: max = volatility
#     if volatility < min: min = volatility
#     volatilities.append([country, volatility])

volatilities = [['Afghanistan', 5.451762045764935], ['Algeria', 0.24480861057222897], ['Armenia', 0.15574085466112794], ['Azerbaijan', 0.039111317009321], ['Bangladesh', 0.027109521326183172], ['Benin', 0.05290083068778323], ['Bhutan', 0.04807347084783716], ['Bolivia', 0.0499361934806208], ['Burkina Faso', 0.02272942511024886], ['Burundi', 0.05200812929686041], ['Cambodia', 0.07683179017945005], ['Cameroon', 0.07906990993770957], ['Cape Verde', 0.03910145134791838], ['Central African Republic', 0.25603448351175984], ['Chad', 0.17909409456926992], ['Colombia', 0.18560229585870522], ['Congo', 0.3766406092190523], ["Cote d'Ivoire", 0.0834488583353887], ['Democratic Republic of the Congo', 0.21341982564224807], ['Djibouti', 0.03815978082907376], ['Egypt', 0.1427341426899759], ['El Salvador', 0.07835434876389584], ['Ethiopia', 0.08143275599279524], ['Gambia', 0.10626436660745985], ['Georgia', 0.045395634730132244], ['Ghana', 3.8070776003012607], ['Guatemala', 0.06519401838063224], ['Guinea-Bissau', 0.09850211608878758], ['Haiti', 0.28641289846334816], ['India', 0.046570525167371625], ['Indonesia', 0.13004520670769504], ['Iran  (Islamic Republic of)', 0.1335352985426966], ['Iraq', 0.06971485707193184], ['Jordan', 14.461277844040378], ['Kenya', 0.04755830735825581], ['Kyrgyzstan', 0.10742095579079329], ["Lao People's Democratic Republic", 0.07430618455796492], ['Lebanon', 0.3265753371087339], ['Lesotho', 0.05529449555225416], ['Liberia', 0.8244212696397196], ['Madagascar', 0.06086402430107554], ['Malawi', 0.08708674136743533], ['Mali', 0.027980655481583523], ['Mauritania', 0.05014991464855883], ['Mozambique', 0.10239838910437424], ['Myanmar', 11.655285769086298], ['Nepal', 0.020857454503145564], ['Niger', 0.04304875062338448], ['Nigeria', 0.21000217310949776], ['Pakistan', 0.04070805411961563], ['Peru', 0.035458610137697646], ['Philippines', 0.1334871240165406], ['Rwanda', 0.29973833050876253], ['Senegal', 0.03131421026203454], ['Sri Lanka', 0.03446938503684106], ['State of Palestine', 0.30603206110816833], ['Sudan', 0.05020932627381398], ['Swaziland', 0.05931642724703113], ['Tajikistan', 0.07118603750613697], ['Timor-Leste', 0.20599675925925878], ['Turkey', 0.4693287895548425], ['Uganda', 0.06047264402477273], ['Ukraine', 0.10995917566824542], ['United Republic of Tanzania', 0.051113477868391585], ['Yemen', 0.15213629731442796], ['Zambia', 0.15991687303036534], ['Zimbabwe', 0.2170282519567649]]

volatilities = list(map(lambda x: [x[0], i_sqrt(x[1], 10)], volatilities))

# for vol in sorted(volatilities, key=lambda x: x[1], reverse=True):
#   print("{0}: {1}".format(vol[0], vol[1]))

options = { 'min': 0, 'max': 15 }

plot_geochart("volatility", volatilities, options)
