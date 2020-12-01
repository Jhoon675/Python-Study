from hdfs import InsecureClient # hdfs 모듈에서 WebHDFS 모듈 임포트

#접속 테스트
client = InsecureClient("http://192.168.56.100:50070", user="hadoop")
print(client.status)

# 파일 탐색 함수
def list_files(path): # path 경로 내의 파일을 출력한다.
    files = client.list(path)

    if len(files) == 0:
        print("File Not Found")
    else:
        for file in files:
            print("File:", file)


# 파일 디렉터리 생성
def makedir_test(path):
    """path 경로를 hdfs에 생성"""
    client.makedirs(path)



def delete_test(path, r=True):
    # recursive = True: 디렉터리의 경우 하위 디렉터리도 함께 삭제
    client.delete(path, recursive=r)



def write_test(path, text, encoding="utf-8"):
    """path 경로의 파일에 text를 저장"""
    with client.write(path, encoding=encoding) as writer:
        writer.write(text)



def read_test(path, encoding="utf-8"):
    """path 경로의 파일을 읽어서 출력"""
    with client.read(path, encoding=encoding) as reader:
        data = reader.read()

    print("Hadoop Read:",data)



if __name__== "__main__":
    list_files("/example") # / 아래의 파일 목록을 출력
    # makedir_test("/example/pyhadoop")
    # delete_test("/example/myhadoop")
    # write_test("/example/myhadoop/test.txt", "Hello Hadoop")
    # read_test("/example/myhadoop/test.txt")