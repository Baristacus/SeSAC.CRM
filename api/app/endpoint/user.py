from flask import request
from flask_restful import Resource
from app.models import User


class UserList(Resource):
    def get(self):
        # 페이지네이션
        page = request.args.get("page", 1, type=int)  # 기본 1페이지부터 시작
        per_page = request.args.get("per_page", 10, type=int)  # 페이지당 10개씩

        # 검색조건
        name = request.args.get("name")
        age = request.args.get("age")
        gender = request.args.get("gender")

        # 기본쿼리
        query = User.query

        # 검색조건이 있을 경우 필터링
        if name:
            query = query.filter(User.Name == name)
        if age:
            query = query.filter(User.Age == age)
        if gender:
            query = query.filter(User.Gender == gender)

        # 페이지네이션 적용
        pagenation = query.paginate(page=page, per_page=per_page)

        return [
            {
                "id": user.Id,
                "name": user.Name,
                "gender": user.Gender,
                "birthday": user.Birthday,
                "age": user.Age,
                "address": user.Address,
                "total_count": pagenation.total,
                "current_page": pagenation.page,
                "per_page": pagenation.per_page,
                "has_next": pagenation.has_next,
                "has_prev": pagenation.has_prev,
                "next_page": pagenation.next_num,
                "prev_page": pagenation.prev_num,
                "total_page": pagenation.pages,
            }
            for user in pagenation.items
        ]


class UserDetail(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return {
                "Id": user.Id,
                "Name": user.Name,
                "Gender": user.Gender,
                "Birthday": user.Birthday,
                "Age": user.Age,
                "Address": user.Address,
            }
        else:
            return {"message": "사용자를 찾을 수 없습니다."}, 404
