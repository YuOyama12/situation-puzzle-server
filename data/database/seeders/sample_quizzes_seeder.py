from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.settings import DB_URL
from data.database.seeders.constants import SAMPLE_QUIZ_ID, SAMPLE_QUIZ_USER_ID
from data.database.tables.quiz import Quiz

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

def execute():
    """
    quizzesテーブル内にサンプル用の問題を追加する
    """
    session = SessionLocal()

    try:
        quizzes = [
            Quiz(
                id=SAMPLE_QUIZ_ID,
                user_id=SAMPLE_QUIZ_USER_ID,
                title = "ウミガメのスープ",
                question = "ある男性が、海の近くのレストランでウミガメのスープを注文しました。彼はスープを一口飲んだところで、シェフに問いかけました。『すみません、これはウミガメのスープで合っていますか？』シェフは『はい、お客様が召し上がったのは間違いなくウミガメのスープですよ』と答えました。男性は会計を済ませ、家に帰ると自殺してしまいました。\n\nいったいなぜでしょう？",
                answer = "男性はかつて仲間と海で遭難し、無人島にたどり着きました。そこは食料が何もない孤島。体力のない者からどんどん死んでしまい、生き残っている者は仲間の死肉を食べて空腹を満たそうとします。しかし、1人の男性はそれを拒否し、みるみるうちにやつれていきます。そこで仲間たちは『ウミガメのスープを作ったから食べなさい』と偽り人肉のスープを飲ませ、救出まで生き延びさせました。男性はレストランで食べたウミガメのスープと、かつて食べたスープの味が違っていることに気づき、過去の真相を知って自殺に至ったのでした。",
                
            ),
            Quiz(
                user_id=SAMPLE_QUIZ_USER_ID,
                title = "逆走するタクシー運転手",
                question = "タクシー運転手が一方通行を逆走しても警官に咎められなかった。\nなぜ？",
                answer = "運転手は車に乗っておらず、歩いて一方通行の道を逆方向に進んでいただけだったため。\n歩行者には一方通行の規則が適用されないため、警官に咎められなかった。",
                
            ),
            Quiz(
                user_id=SAMPLE_QUIZ_USER_ID,
                title = "研究者",
                question = "ある男は肉食獣の研究者だった。彼はその日、小さな娘と一緒にいた眼の前でライオンが歩いている。もちろん彼の飼っているライオンではない。娘は怖がって泣いているが、彼は逃げようとしないし、恐怖を感じていなかった。\nどういう状況？",
                answer = "休日のとある日。娘と動物園にいた。ライオンは檻の中にいるので逃げ出す必要がない。",
            ),
            Quiz(
                user_id=SAMPLE_QUIZ_USER_ID,
                title = "完成",
                question = "ある男は何かを完成させようと作業をしていた。いつも完成させることはできるのだが、完成したらすぐに壊してしまう。完成したものは完璧だ。気に入らなかったわけではない。\nどういう状況？",
                answer = "男はルービックキューブをしていた。\n完成したらすぐに壊して何度も完成させ、完成までのタイム短縮の努力をしていたのだ。",
            ),
            Quiz(
                user_id=SAMPLE_QUIZ_USER_ID,
                title = "ロボット発明家",
                question = "ロボット発明で有名な発明家がいた。彼は7体のロボットを開発した。\n最新ロボットの発表会を終えた彼は、プライベートの時間を過ごしていた。\nすると彼は「あなたはロボットか？」と確認された上に、証明するためのテストまでやらされた。彼は顔写真付きの免許証を持っているし、ワイドショーにも出演して顔を知られているにも関わらずだ。\nどういう状況？",
                answer = "とある通販サイトにログインしようとしてCAPTCHA認証の中でロボットかどうかを確認された。",
            ),
        ]

        session.add_all(quizzes)
        session.flush()
        session.commit()
        print("Inserting sample quizzes was completed successfully!")    
    except:
        session.rollback()
    finally:
        session.close()
