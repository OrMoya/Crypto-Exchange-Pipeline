import etl_extract
import etl_load

def run() -> None: 
    etl_extract.run()
    etl_load.run()
    
if __name__ == '__main__':
    run()

