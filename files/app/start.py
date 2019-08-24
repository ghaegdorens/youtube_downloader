import os
import pandas as pd
import io


def main():
    
    o=os.popen('pip list --outdated').read()
    
    if (o):
        package_len = o.index('Version')
        version_len = o.index('Latest') - o.index('Version')
        latest_len =  o.index('Type') - o.index('Latest')
        type_len = len(o.split('\n')[0]) - o.index('Type')
    
        df = pd.read_fwf(io.StringIO(o), widths=[package_len, version_len, latest_len, type_len])

        df_filtered = df[df.Package == 'boto3']
        if (df_filtered.at[1,'Version'] != df_filtered.at[1,'Latest']):
            print('update package')
            #o=os.popen('pip install -U youtube-dl').read()
            #print(o)

if __name__ == '__main__':
    main()
    