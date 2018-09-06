from app.lib.enums import PendingStatus


class DriftsViewModel:
    def __init__(self, drifts,uid):
        self.drifts = []
        self.uid = uid
        self.parse_drifts(drifts)

    def parse_drifts(self, drifts):
        self.drifts = [self.parse_drift(drift) for drift in drifts]

    def parse_drift(self, drift):
        you_are = 'requester' if self.uid==drift.requester_id else 'gifter'
        operator = drift.gifter_nickname if you_are == 'requester' else drift.requester_nickname
        return dict(
            book_img=drift.book_img,
            book_title=drift.book_title,
            book_author=drift.book_author,
            date=drift.create_datetime,
            recipient_name=drift.recipient_name,
            mobile=drift.mobile,
            drift_id=drift.id,
            message=drift.message,
            you_are=you_are,
            status=drift.pending,
            status_str=PendingStatus.status_str(you_are,drift.pending),
            address=drift.address,
            operator=operator
        )
