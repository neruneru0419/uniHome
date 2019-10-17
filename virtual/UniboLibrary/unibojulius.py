import subprocess


def julius():
    subprocess.Popen(
        'julius -C ~/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram ~/julius/dict/hello -input mic -module', shell=True)
