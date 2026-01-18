import subprocess
import sys
import os

def install_packages():
    
    packages = [
        "aiogram==2.25.1",
        "Pillow==10.1.0",
        "python-dotenv==1.0.0",
        "aiofiles==23.2.1"
    ]
    
    print("="*60)
    print("УСТАНОВКА ЗАВИСИМОСТЕЙ ДЛЯ БОТА")
    print("="*60)
    
    print("\n🔧 Обновление pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    
    for package in packages:
        print(f"\n📦 Устанавливаю {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} успешно установлен")
        except subprocess.CalledProcessError as e:
            print(f"❌ Ошибка при установке {package}: {e}")
            package_name = package.split('==')[0]
            print(f"🔄 Пробую установить {package_name} без указания версии...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
                print(f"✅ {package_name} установлен")
            except:
                print(f"❌ Не удалось установить {package_name}")
    
    print("\n📁 Создание структуры папок...")
    folders = ["photos", "captchas", "backups", "balance_proofs"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"✅ Создана папка: {folder}")
    
    print("\n" + "="*60)
    print("🎉 ВСЕ ЗАВИСИМОСТИ УСТАНОВЛЕНЫ!")
    print("="*60)
    print("\n📋 Созданы папки:")
    print("• photos/ - для изображений товаров")
    print("• captchas/ - для капч")
    print("• backups/ - для резервных копий")
    print("• balance_proofs/ - для скриншотов оплаты")
    print("\n🚀 Запуск бота: python Bot_Ckam_копия.py")
    print("="*60)

if __name__ == "__main__":
    install_packages()