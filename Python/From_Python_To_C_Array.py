import numpy as np

Q2_13_SCALE = 2 ** 13  # 8192

def array_to_txt(arr, size=None, output_file="output.txt"):
    arr = np.asarray(arr).flatten()[:size]
    with open(output_file, "w") as f:
        if np.iscomplexobj(arr):
            arr_real = (arr.real * Q2_13_SCALE).astype(np.int32)
            arr_imag = (arr.imag * Q2_13_SCALE).astype(np.int32)
            for r, i in zip(arr_real, arr_imag):
                f.write(f"{{{r}, {i}}},\n")
        else:
            arr_fixed = (arr * Q2_13_SCALE).astype(np.int32)
            for v in arr_fixed:
                f.write(str(v) + ",\n")