# pokemon_StatusCalcuration

ポケモンの種族値・個体値・努力値・性格補正・レベルから、実数値（H/A/B/C/D/S）を計算するGUIツールです。

> 2024年3月頃、学生時代に作った小さなツールです。

## 使い方

1. 各ステータスの種族値・個体値・努力値を入力し、A〜Sの性格補正（`x1.1` / `-` / `x0.9`）を選ぶ
2. レベルを選ぶ
3. 「実行」を押すと実数値が表示される（「リセット」で入力をクリア）

## 計算式

- HP: `floor((種族値×2 + 個体値 + 努力値/4) × Lv/100 + Lv + 10)`
- HP以外: `floor(((種族値×2 + 個体値 + 努力値/4) × Lv/100 + 5) × 性格補正)`

## 動かし方

Python標準ライブラリ（tkinter）のみで動きます。

```bash
python pokemon_StatusCalcuration/pokemon_StatusCalcuration.py
```

Visual Studio の場合は `pokemon_StatusCalcuration.sln` を開いて実行することもできます。
