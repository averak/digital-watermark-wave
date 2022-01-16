import argparse

from service.wave_service import WaveService
from repository.wave_repository import WaveRepository

# アプリケーションサービスを作成
wave_repository = WaveRepository()
wave_service = WaveService(wave_repository)

# アプリケーションのオプションを定義
# --helpでヘルプを表示できます
parser: argparse.ArgumentParser = argparse.ArgumentParser()
parser.add_argument('-r', '--record',
                    help='音声を録音',
                    action='store_true')
parser.add_argument('-c', '--clear',
                    help='音声データを全削除',
                    action='store_true')
args = parser.parse_args()

if args.record:
    wave_service.record_wave()

if args.clear:
    wave_service.clear_all_data()
