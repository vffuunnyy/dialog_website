from pydantic import BaseModel


class NginxHeadersModel(BaseModel):
    host: str = None
    x_real_ip: str = None
    x_forwarded_for: str = None
    x_forwarded_proto: str = None
    user_agent: str = None
