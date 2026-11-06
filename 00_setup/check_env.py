"""환경 확인 스크립트: 설치된 패키지 버전, GPU 사용 가능 여부, MuJoCo 환경 생성을 점검한다.

실행: .venv\\Scripts\\python.exe 00_setup\\check_env.py
(reset/step 루프와 GIF 만들기는 S0 과제라서 여기서는 하지 않는다.)
"""
import platform
import sys


def section(title: str) -> None:
    print(f"\n== {title} ==")


def main() -> int:
    ok = True

    section("Python")
    print(sys.version.split()[0], platform.system(), platform.machine())

    section("PyTorch")
    try:
        import torch

        print("torch", torch.__version__)
        cuda = torch.cuda.is_available()
        print("CUDA available:", cuda)
        if cuda:
            print("GPU:", torch.cuda.get_device_name(0))
            print("CUDA build:", torch.version.cuda)
        else:
            ok = False
            print("! CUDA를 쓸 수 없습니다. CPU 전용 PyTorch가 설치됐는지 확인하세요 (00_setup/README.md).")
    except ImportError:
        ok = False
        print("! torch가 설치되지 않았습니다.")

    section("Packages")
    for name in ("torchvision", "mujoco", "gymnasium", "stable_baselines3", "Box2D"):
        try:
            module = __import__(name)
            print(name, getattr(module, "__version__", "?"))
        except ImportError:
            ok = False
            print(f"! {name} 패키지가 설치되지 않았습니다.")

    section("HalfCheetah-v5")
    try:
        import gymnasium as gym

        env = gym.make("HalfCheetah-v5")
        env.reset(seed=0)
        print("observation space:", env.observation_space)
        print("action space:", env.action_space)
        env.close()
    except Exception as exc:  # noqa: BLE001 - show any setup problem as-is
        ok = False
        print("! 환경을 만들지 못했습니다:", exc)

    section("Result")
    print("OK - S0 과제(random_agent.py)로 넘어가세요." if ok else "문제가 있습니다. 위의 ! 표시를 확인하세요.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
