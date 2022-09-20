from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    env = i['env']
    if '+PYTHONPATH' not in env: env['+PYTHONPATH']=[]
    if '+C_INCLUDE_PATH' not in env: env['+C_INCLUDE_PATH']=[]
    if '+CXX_INCLUDE_PATH' not in env: env['+CXX_INCLUDE_PATH']=[]
    if '+LD_LIBRARY_PATH' not in env: env['+LD_LIBRARY_PATH']=[]
    if '+DYLD_FALLBACK_LIBRARY_PATH' not in env: env['+DYLD_FALLBACK_LIBRARY_PATH']=[]
    env['+C_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'install', 'include'))
    env['+CXX_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'install', 'include'))
    env['+LD_LIBRARY_PATH'].append(os.path.join(os.getcwd(), 'install', 'lib'))
    env['+DYLD_FALLBACK_LIBRARY_PATH'].append(os.path.join(os.getcwd(), 'install', 'lib'))
    env['+PYTHONPATH'].append(os.path.join(os.getcwd(), 'install', 'python'))

    return {'return':0}
