import cj_function_lib as cj
import init_file as variables

urban = """  1 URHD                                Residential-High Density   0.600   0.440
       0.240   0.180 225.000   0.750 550.000 223.000   7.200  98.0
  2 URMD                              Residential-Medium Density   0.380   0.300
       0.240   0.180 225.000   0.750 550.000 223.000   7.200  98.0
  3 URML                             Residential-Med/Low Density   0.200   0.170
       0.240   0.180 225.000   0.750 460.000 196.000   6.000  98.0
  4 URLD                                 Residential-Low Density   0.120   0.100
       0.240   0.180 225.000   0.750 460.000 196.000   6.000  98.0
  5 UCOM                                              Commercial   0.670   0.620
       0.280   0.180 200.000   1.600 420.000 240.000   5.500  98.0
  6 UIDU                                              Industrial   0.840   0.790
       0.140   0.180 400.000   2.350 430.000 104.000   5.600  98.0
  7 UTRN                                          Transportation   0.980   0.950
       0.120   0.180 340.000   3.900 480.000 212.000   6.300  98.0
  8 UINS                                           Institutional   0.510   0.470
       0.120   0.180 340.000   3.900 480.000 212.000   6.300  98.0
  9 URBN                                             Residential   0.380   0.300
       0.240   0.180 225.000   0.750 550.000 223.000   7.200  98.0
"""

fileName = "urban.dat"
cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, urban)
#print fileName