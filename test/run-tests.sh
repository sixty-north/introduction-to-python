for OFS in ../v01 ../v02 ../v03 ../v04/zorkalike; do
    PYTHONPATH=$OFS pytest test_zorkalike.py
done
