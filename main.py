from queries.crud import create_db, fill_db
from queries.queries import get_user_reservations, get_relax_base_rooms, popular_relax_bases_filter, total_spent, \
    cancel_reservation

get_user_reservations(1)
get_relax_base_rooms(2)

total_spent(5)
popular_relax_bases_filter()

cancel_reservation(1)
