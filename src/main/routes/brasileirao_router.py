from fastapi import APIRouter
from src.application.controllers import *

router = APIRouter()

@router.get('/clubes')
def list_all_clubs():
    list_all_clubs_controller = ListAllClubsController()
    response = list_all_clubs_controller.handler()
    return response

@router.get('/clubes/{clube_id}')
def list_one_club(clube_id: int):
    list_one_club_controller = ListOneClubController()
    response = list_one_club_controller.handler(clube_id)
    return response

@router.get('/clubes/{clube_id}/details')
def list_club_details(clube_id: int):
    list_club_details_controller = ListClubDetailsController()
    response = list_club_details_controller.handler(clube_id)
    return response