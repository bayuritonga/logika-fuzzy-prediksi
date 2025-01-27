import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def fuzzy_adjustment(predicted_price, market_condition):
    # Definisikan variabel fuzzy untuk kondisi pasar
    kondisi_pasar = ctrl.Antecedent(np.arange(0, 101, 1), 'kondisi_pasar')
    harga_disesuaikan = ctrl.Consequent(np.arange(0, 1000000, 1), 'harga_disesuaikan')

    # Fungsi keanggotaan untuk kondisi pasar
    kondisi_pasar['bearish'] = fuzz.trimf(kondisi_pasar.universe, [0, 0, 50])
    kondisi_pasar['stable'] = fuzz.trimf(kondisi_pasar.universe, [30, 50, 70])
    kondisi_pasar['bullish'] = fuzz.trimf(kondisi_pasar.universe, [50, 100, 100])

    # Fungsi keanggotaan untuk harga disesuaikan
    harga_disesuaikan['murah'] = fuzz.trimf(harga_disesuaikan.universe, [0, 0, 300000])
    harga_disesuaikan['normal'] = fuzz.trimf(harga_disesuaikan.universe, [200000, 400000, 600000])
    harga_disesuaikan['mahal'] = fuzz.trimf(harga_disesuaikan.universe, [500000, 1000000, 1000000])

    # Aturan fuzzy
    rule1 = ctrl.Rule(kondisi_pasar['bearish'], harga_disesuaikan['murah'])
    rule2 = ctrl.Rule(kondisi_pasar['stable'], harga_disesuaikan['normal'])
    rule3 = ctrl.Rule(kondisi_pasar['bullish'], harga_disesuaikan['mahal'])

    # Membuat sistem kontrol
    sistem_penyesuaian = ctrl.ControlSystem([rule1, rule2, rule3])
    penyesuaian = ctrl.ControlSystemSimulation(sistem_penyesuaian)

    # Input ke sistem fuzzy
    penyesuaian.input['kondisi_pasar'] = market_condition

    # Hitung output
    penyesuaian.compute()

    # Mengembalikan harga yang disesuaikan
    return penyesuaian.output['harga_disesuaikan']