import requests
from app.schemas import UserResponse
def find_user(user_id):

    for attempts in range(2):

        try:

            response = requests.get(
                f"https://jsonplaceholder.typicode.com/users/{user_id}",
                timeout=3
            )

        except requests.exceptions.Timeout:

            if attempts == 1:

                return UserResponse(
                    success=False,
                    data=None,
                    error="Timeout Error",
                    error_type="Timeout"
                )
            continue

        except requests.exceptions.RequestException:

            return UserResponse(
                success=False,
                data=None,
                error="The API call failed",
                error_type="Failed call"
            )

        if response.status_code == 200:

            return UserResponse(
                success=True,
                data=response.json(),
                error=None,
                error_type=None
            )

        elif response.status_code == 404:

            return UserResponse(
                success=False,
                data=None,
                error="The user does not exists",
                error_type="Invalid API call"
            )

        return UserResponse(
            success=False,
            data=None,
            error="The call is invalid",
            error_type="Invalid API"
        )

