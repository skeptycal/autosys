######################################
# Reference: https://stackoverflow.com/a/52713738/9878098
import sys, os, inspect, time

time_start = 0.0                    # initial start time

def trace_libary_init():
    global time_start

    time_start = time.time()      # when the program started

def trace_library_do(relative_frame, msg=""):
    global time_start

    time_now = time.time()

        # relative_frame is 0 for current function (this one),
        # 1 for direct parent, or 2 for grand parent..

    total_stack         = inspect.stack()                   # total complete stack
    total_depth         = len(total_stack)                  # length of total stack
    frameinfo           = total_stack[relative_frame][0]    # info on rel frame
    relative_depth      = total_depth - relative_frame      # length of stack there

        # Information on function at the relative frame number

    func_name           = frameinfo.f_code.co_name
    filename            = os.path.basename(frameinfo.f_code.co_filename)
    line_number         = frameinfo.f_lineno                # of the call
    func_firstlineno    = frameinfo.f_code.co_firstlineno

    fileline            = "%s:%d" % (filename, line_number)
    time_diff           = time_now - time_start

    print("%13.6f %-20s %-24s %s" % (time_diff, fileline, func_name, msg))

################################

def trace_do(msg=""):
    trace_library_do(1, "trace within interface function")
    trace_library_do(2, msg)
    # any common tracing stuff you might want to do...

################################

def main(argc, argv):
    rc=0
    trace_libary_init()
    for i in range(3):
        trace_do("this is at step %i" %i)
        time.sleep((i+1) * 0.1)         # in 1/10's of a second
    return rc

rc=main(sys.argv.__len__(), sys.argv)
sys.exit(rc)
