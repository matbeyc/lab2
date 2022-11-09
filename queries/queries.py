import sqlite3


def get_user_reservations(user_id):
    """
    Поиск всех покупок пользователя и сортировка их по дате покупки от последней покупки к первой(запрос нужен, чтобы отображать резервации в лк пользователя)
    :param user_id:
    :return:
    """
    connection = sqlite3.connect("practice1")
    cursor = connection.cursor()

    response = cursor.execute(f'''
            SELECT reservation.price, reservation.reservation_timestamp FROM reservation
            JOIN user
            ON reservation.user_id = user.id
            WHERE user.id = {user_id}
            ORDER BY reservation.reservation_timestamp desc;
            
                ''')
    print(response.fetchall())


def get_relax_base_rooms(relax_base_id):
    """
    Поиск топ 3-ех самых дешевых комнат по базе отдыха(запрос нужен, чтобы отображать эти комнаты на  карточке базы отдыха)
    :param relax_base_id:
    :return:
    """
    connection = sqlite3.connect("practice1")
    cursor = connection.cursor()

    response = cursor.execute(f'''
                SELECT relax_base_room.name FROM relax_base_room
                JOIN relax_base
                ON relax_base_room.relax_base_id = relax_base.id
                WHERE relax_base.id = {relax_base_id}
                ORDER BY relax_base_room.price_for_day
                LIMIT 3
                ;

                    ''')
    print(response.fetchall())


def popular_relax_bases_filter():
    """
    Сортировка баз отдыха от самых популярных.(Запрос пригодится для главной странице, чтобы показывать сначала популярные базы отдыха)
    :return:
    """
    connection = sqlite3.connect("practice1")
    cursor = connection.cursor()

    response = cursor.execute(f'''
                    SELECT COUNT(reservation.id) as reservations_amount, relax_base.name from reservation
                    JOIN relax_base_room
                    ON reservation.relax_base_room_id = relax_base_room.id
                    JOIN relax_base
                    ON relax_base.id = relax_base_room.relax_base_id
                    WHERE reservation.status != 'CANCELLED'
                    GROUP BY relax_base.id
                    ORDER BY reservations_amount desc;
                        ''')
    print(response.fetchall())


def total_spent(user_id):
    connection = sqlite3.connect("practice1")
    cursor = connection.cursor()

    """
    Запрос выводит сколько всего денег потратил пользователь. Может пригодится, если, допустим, будет бонусная система и чтобы пользователь видел сколько ему не хватает, чтобы получить те или иные привелегии
    """

    response = cursor.execute(f'''
                    SELECT SUM(reservation.price) as total FROM reservation
                    WHERE reservation.user_id = {user_id} AND reservation.status != 'CANCELLED'
                    GROUP BY reservation.user_id;
                        ''')
    print(response.fetchall())


def cancel_reservation(reservation_id):
    """
    Запрос на отмену резервации
    :param reservation_id:
    :return:
    """
    connection = sqlite3.connect("practice1")
    connection.execute(f'''
    UPDATE reservation
    SET status = 'CANCELLED',
        unreserved = datetime('now')
    WHERE reservation.id = {reservation_id};
    ''')
    connection.commit()


def delete_comment(comment_id):
    """
    Запрос на удаление комментария
    :param comment_id:
    :return:
    """
    connection = sqlite3.connect("practice1")
    connection.execute(f'''
        DELETE FROM comment
        where comment.id = {comment_id};
        ''')
    connection.commit()
