import time
import calculate 

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

def calc_pure_python(desired_width, max_iterations):
    x_step = (float(x2 - x1) / float( desired_width))
    y_step = (float(y1 - y2) / float(desired_width))
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step

    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs = []
    cs = []

    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print("Length of x: ", len(x))
    print("Total elements: ", len(zs))

    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    # print(calculate_z_serial_purepython.func_name  + " took ",secs, " seconds" )
    print("calculate_z_serial_purepython took ", secs, " seconds" )

    assert sum(output) == 33219980

if __name__ == "__main__":
    calc_pure_python(desired_width = 1000, max_iterations = 300)
