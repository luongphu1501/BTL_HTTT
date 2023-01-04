from .models import Benh, TrieuChung
import numpy as np

def cbr(problem):
    list_benh = Benh.objects.all()
    result = 0
    index = 0
    problem = np.array(problem)

    for case in list_benh:
        list_ts = [];
        list_gt = [];
        list_tc = case.trieuchung_set.all().order_by("ki_hieu")
        for tc in list_tc:
            list_ts.append(tc.trongso)
            list_gt.append(tc.gia_tri)
        list_ts = np.array(list_ts)
        list_gt = np.array(list_gt)
        kq = (list_ts*(1 - np.abs(problem - list_gt))).sum()/ list_ts.sum()
        if kq > result:
            result= kq
            index = case.id
            print(kq)
    return index



