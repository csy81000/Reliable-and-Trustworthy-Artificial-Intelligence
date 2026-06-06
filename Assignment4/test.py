
import subprocess
import sys

def main():
    print("[과제 #4] alpha-beta-CROWN 검증을 시작합니다... (시간이 조금 걸릴 수 있습니다)")
    cmd = [sys.executable, "abcrown.py", "--config", "my_config.yaml"]
    
    # 텍스트 출력을 그대로 가져옵니다.
    result = subprocess.run(cmd, capture_output=True, text=True)

    print("\n===========================================")
    print("           [검증 표준 출력 (결과)]           ")
    print("===========================================")
    print(result.stdout)

    if result.stderr:
        print("\n===========================================")
        print("               [검증 에러 로그]              ")
        print("===========================================")
        print(result.stderr)

if __name__ == "__main__":
    main()
