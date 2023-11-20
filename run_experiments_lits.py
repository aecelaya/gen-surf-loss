import subprocess

losses = ["dice", "dice_ce", "gdl", "bl", "hl", "gsl"]

for loss in losses:
    cmd = "python main.py --exec-mode train "
    cmd += "--data /path/to/lits-binary.json "
    cmd += "--numpy /path/to/numpy/ "
    cmd += "--results /path/to/results/{} ".format(loss)
    cmd += "--loss {} ".format(loss)
    if loss == "gsl":
        cmd += "--use-precomputed-class-weights "
    cmd += "--seed 42 "
    cmd += "--patch-size 256 256 128 "
    cmd += "--learning-rate 0.0003 "
    cmd += "--amp "
    cmd += "--epochs 250 "
    cmd += "--gpus 0 1"

    subprocess.call(cmd, shell=True)
