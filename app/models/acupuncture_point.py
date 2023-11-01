from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

# declarative_base() は、クラス定義を使用してSQLAlchemyテーブルを定義するための基底クラスを作成します。
Base = declarative_base()

class AcupuncturePoint(Base):
    # __tablename__ 属性はこのモデルによってデータベース内で使用されるテーブルの名前を設定します。
    __tablename__ = "acupuncture_points"
    
    # 各ツボの一意の識別子であり、データベース内でプライマリキーとして機能します。
    id = Column(Integer, Sequence("acupuncture_point_id_seq"), primary_key=True)
    
    # ツボの名前を格納するためのカラムです。
    name = Column(String)
    
    # ツボの説明や効能を格納するためのカラムです。
    description = Column(String)
