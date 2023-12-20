# 코드 기본 형식

## import 시 주로 사용하는 방식
from classes_formats import Person, Arithmetics, Class_name

# class basic ocde
class Class_name:
    def __init__(self):
        pass

    def function_name(): # self 키워드 필요 (class 소속 확인용)
        try: 
            pass        # 업무 코드
        except:
            pass        # 업무 코드 문제 발생 시 대처 코드
        finally:
            pass        # try나 except이 끝난 후 무조건 실행 코드
        pass    # 내용 넣기
        return 0

def function_name(): # self 키워드 필요 (class 소속 확인용)
    try: 
        pass        # 업무 코드
    except:
        pass        # 업무 코드 문제 발생 시 대처 코드
    finally:
        pass        # try나 except이 끝난 후 무조건 실행 코드
    pass    # 내용 넣기
    return 0

if __name__ == "__main__":
    try: 
        pass        # 업무 코드
    except:
        pass        # 업무 코드 문제 발생 시 대처 코드
    finally:
        pass        # try나 except이 끝난 후 무조건 실행 코드

    pass

