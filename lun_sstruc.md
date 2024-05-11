## 搜尋 Hubert repr 分析 v.s phonetic

第三章 語音離散單元

-----------------

# 大綱

## Ch 2. 背景
   * 技術
      * (0) NN 基礎
      * (0) Model archs
      * (0) SSL 表徵
      * (0) 離散表徵
      * (0) 文字 tokenization
      // 語音學 alignment?
      // 語意層面？
      // 要學那篇做 syntax 嗎？
   * Related works
      * HuBERT & its representations analysis
      * Speech discretization methods & its applications
         --> e.g. SpeechTokenizer
      * PseudoWord Trials
      // Current Speech model Analysis?
         // Seamless M4T alignment?

## Ch 3. Single unit 
   hubert units的大量完整分析
   * (0) 離散單元取得方式
      * (0) HuBERT...
      * (0) EnCodec
      * (0) Whisper
      * purity (reproduce HuBERT 前作）
      * encodec
      * whisper
   * 嘗試不同 settings
      * 但hubert unit分析上有不足
      * 一個phone對應多個units，pattern未明
   * 所以下一章：探討multi-unit分析

## Ch 4. 語音離散表徵做 BPE 的嘗試
   * (0) 動機簡介
   * (0) (multiunit) tokenization 方式
      * (0) BPE
      * (0) WordPiece
      // word separated
   * analysis
      * (0) 分析標準
         * (0) Purity --> alignment to phoneme/text tokens (seg?)
            * (0) 跟 phoneme 互對
            * (0) 跟 token 或 word 互對？
         * (0) Compression rate
      * (0) 實驗設定
         * application --> IC ==> "Compression & purity v.s performance"
         * (0) 實驗資料集：LibriSpeech, CommonVoice
            * (0) 資料量：Token learning ratio
      * (0) 結果分析
      * (0) 本章節總結
   * application --> (Ch 5?) [Optional]
      * (0) 任務簡介
         * (0) ASR
         * (0) ST
         * (0) TTS (LM rescoring)
         * (0) LM?
      * (0) 實驗分析標準
         * Compression & purity v.s performance
      * (0) 實驗設定
      * (0) 結果分析
      * (0) 本章總結

## Ch 0. 重啟大綱
   * 新的研究動機

## Ch 1. 導論
   * 研究動機
   * 研究主題
   * 相關研究
   * 章節安排

## Ch 2. 背景知識
   * 深層類神經網路（deep neural network）
      * 簡介
      * 卷積（convolutional）類神經網路
      * 遞迴（recurrent）類神經網路
      * 序列至序列（sequence-to-sequence）模型與專注機制（attention mechanism）
      * 轉換器（Transformer）類神經網路
   * 表徵（representation）學習
      * 自監督式（self-supervised）學習表徵
         * 語言模型（langauge model）
         * 遮罩語言模型（masked langauge model）
      * 向量離散化（vector quantization）
         * k-平均（k-means）演算法
      * 文字表徵學習
      * 語音表徵學習
         * 傳統語音特徵（traditional speech features）
         * 自監督式語音表徵
         * 離散單元（discrete units）

## Ch 3. 語音表徵對語意特徵抽取的分析
   * (1) 簡介
   * (2) 語音表徵
      * 傳統語音特徵
      * 語音詞向量（Audio Word2Vec）
      * 自監督式語音表徵
         * 自監督式預訓練模型
         * 離散單元
   * (3) 實驗設定
      * 語料庫
      * 分析方法
         * 強迫對齊（forced-alignment）
         * 基於相關性（correlation）的語意表徵分析
      * 基線比較模型
      * 實驗細節
   * (4) 結果分析
      * 實驗結果
      * 特性分析
   * (5) 本章總結

## Ch 4. 語音表徵的離散化與其語言模型之分析
   * (1) 簡介
      * 方法動機
   * (2) 離散單元
   * (3) 生成式語音語言模型（Generative Spoken Language Model，GSLM）
   * (4) 基於單字的預訓練
      * 詞向量（Word2Vec）
      * 自監督式學習
   * (5) 結果分析與比較
      * 基於相關性的語意表徵分析
      * 下游任務
         * 任務說明
         * 實驗細節
   * (6) 本章總結

## Ch 5. 結論與展望
   * 研究貢獻與討論
   * 未來展望

# 摘要敘述

　　在語音處理的領域中，特徵抽取（feature extraction）一直是整個系統中相當重要的環節，而在近期深層學習（deep learning）的發展之下，從自然語言處理（natural language processing）領域發展起來的自監督式學習（self-supervised learning）已經在該領域中獲得廣泛的成果，類似的方式也隨之開始被許多人嘗試用於語音訊號的表徵學習（representation learning），並成為一個新的特徵抽取方式，應用於各種語音處理的任務上，期望可以達成比傳統特徵工程（feature engineering）更好的表現。

　　然而，雖然主要都是為了處理人類的語言，自然語言處理的文字和語音處理的語音訊號，在資料量和形式都有著巨大的差異，因此即便使用相似的訓練方式，作為離散（discrete）符號的文字與連續（continuous）訊號的語音仍可能造成訓練後得到的學習表徵差異甚遠。

　　自然語言處理中的向量表徵常以學習語意（semantic features）為號召，可以讓模型學習相似的單字之間共同出現的頻率等特徵。但在語音處理中，複雜且變化多端的訊號卻可能需要先行抽取語音中的聲學特徵（acoustic features）辨別單字，才能進一步處理單字頻率甚至語意資訊等語言特徵（linguistic features）。另外，從資料處理的效率來看，同樣的一句話以語音表徵時所需要的資料長度本身相差數十倍，因此如何讓語音的自監督學習模型能夠更好的借鑒自然語言處理的學習模式，依然是一個相當值得探討的研究方向。

　　為此，本論文旨在分析現有的各種語音表徵是否能夠從語音資料中抽取出類似文字模型的語意特徵，並進一步藉由嘗試對語音表徵進行分群、離散化等操作，使得原先較為複雜的語音表徵可以更加類似於文字模型的學習模式，以期望能夠學到更接近人類語意的向量表徵，並在語音的下游任務——特別是與內容相關的語音辨識和語音翻譯上獲得幫助。

# \_w\_

1. 0
2. 0
3. 0
4. 0
5. 0
6. 0
7. 0
8. 0
9. 0
10. 0
11. 0
12. 0
13. 0
14. 0
15. 0
16. 0

-------------------------------
-------------------------------
-------------------------------
-------------------------------
-------------------------------

# \_u\_
