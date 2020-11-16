import unittest

from OrdersParser import *
from paths import get_order_file_path_for_order_with_file_name


class TestParser(unittest.TestCase):
    def test_get_order_dossiers(self):
        orders_dossiers = {
            "Ordin__nr__701P_din_08_03_2019.txt": (
                "701P",
                188
            ),
            "ORDIN__nr.1084.txt": (
                "1084P",
                402
            ),
            "O_R_D_I_N_nr._747P_din_02.10.2017.txt": (
                "747P",
                272
            ),
            "Ordin_1109P_din_11.11.2011.txt": (
                "1109P",
                407
            ),
            "Ordin-1449P-din-14.07.2014.txt": (
                "1449P",
                317
            ),
            "Ordin_465_din_09.06.2017.txt": (
                "465P",
                198
            ),
            "Ordin_nr._912P_din_24.11.2017.txt": (
                "912P",
                160
            ),
            "Ordin_nr._1848P_din_02.08.2019.txt": (
                "1848P",
                319
            ),
            "Ordin_nr._863P_din_08.07.2020.txt": (
                "863P",
                1
            ),
            "Ordin_772P_din_24.08.2012.txt": (
                "772P",
                410
            ),
            "Ordin_nr__704P_din_11_03_2019.txt": (
                "704P",
                188
            ),
            "Ordin_1910_P_din_18.11.2016.txt": (
                "1910P",
                313
            ),
            "Ordin_263P_din_01.04.2016.txt": (
                "263P",
                289
            ),
            "Ordin_869P_din_26.08.2015.txt": (
                "869P",
                314
            ),
            "Ordin_nr._172P_din_23.02.2018.txt": (
                "172P",
                178
            ),
            "Ordin_nr.747__din_27.07.2011.txt": (
                "747P",
                407
            ),
            "Ordin_nr._664P_din_21.08.2017_MOLDOVA.txt": (
                "664P",
                317
            ),
            "ordin.1187P.din.16.12.2011.txt": (
                "1187P",
                418
            ),
            "Ordin__nr._1768-P-23.07.2019.txt": (
                "1768P",
                294
            )
        }

        for key in orders_dossiers.keys():
            orders_dossiers_parser_results = orders_dossiers[key]

            order_txt_file_path = get_order_file_path_for_order_with_file_name(key)
            order_number = orders_dossiers_parser_results[0]
            dossiers_amount = orders_dossiers_parser_results[1]
            order_results = get_order_dossiers(order_txt_file_path)
            self.assertEqual(order_number, order_results[0])
            self.assertEqual(dossiers_amount, len(order_results[1]))
