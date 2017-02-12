import sys

for i in range(len(sys.argv)):
    if '-p' == sys.argv[i] or '--problem' == sys.argv[i]:
        if '1' == sys.argv[i + 1]:
            import Problema_1.main
        elif '2' in sys.argv:
            import Problema_2.main
        elif '3' in sys.argv:
            # import Problema_3.main
            pass
        elif '4' in sys.argv:
            # import Problema_4.main
            pass
        elif '5' in sys.argv:
            import Problema_5.main
        elif '6' in sys.argv:
            # import Problema_6.main
            pass
        elif '7' in sys.argv:
            import Problema_7.main
        elif '8' in sys.argv:
            import Problema_8.main
        elif '9' in sys.argv:
            # import Problema_9.main
            pass
