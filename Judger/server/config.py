
lang_config={
    'JAVA8':{
        'exe_path':'/usr/bin/java',
        'max_memory':-1,
        'source_name':'Main.java',
        'complication':True,
        'compile_command':'javac {exe_path}/Main.java',
        'run':{
            'args':'-cp {exe_path} -Xss1M -XX:MetaspaceSize=64m -XX:MaxMetaspaceSize=128m -Xms128M -Xmx{max_memory}M Main',
            'seccomp_rule':None,
        }
    },
    'PYTHON35':{
        'exe_path':'/usr/bin/python3.5',
        'source_name':'Main.py',
        'complication': False,
        'compile_command': None,
        'run':{
            'args':'{exe_path}/Main.py',
            'seccomp_rule': 'general',
        }
    },
    'C':{
        'exe_path':'{exe_path}/Main',
        'source_name':'Main.c',
        'complication':True,
        'compile_command':'gcc {exe_path}/Main.c -o {exe_path}/Main',
        'run':{
            'args':'',
            'seccomp_rule':'c_cpp',
        }
    },
    'CPP':{
        'exe_path': '{exe_path}/Main',
        'source_name': 'Main.cpp',
        'complication': True,
        'compile_command': 'g++ {exe_path}/Main.cpp -o {exe_path}/Main',
        'run': {
            'args': '',
            'seccomp_rule': 'c_cpp',
        }
    },
    'PYTHON27':{
        'exe_path':'/usr/bin/python2.7',
        'source_name':'Main.py',
        'complication': False,
        'compile_command':None,
        'run':{
            'args':'{exe_path}/Main.py',
            'seccomp_rule': 'general',
        }
    }
}

sys_config = {
    #日志文件所在路径
    'logfile':'/usr/eagle-oj-judger/Judger/judge.log',
    #提交的代码和测试用例存储的位置
    'outfile': '/usr/JudgeResult',
    #是否删除每次所产生的文件
    'removefile':True,
    #model包的路径
    'model':'/usr/eagle-oj-judger/Judger/model',
    #server包的路径
    'server':'/usr/eagle-oj-judger/Judger/server',
    #指定运行系统的uid和gid,为了保证系统的安全运行请务必创建新用户
    'uid':1001,
    'gid':1001
}
