import json

from moto.core.responses import BaseResponse
from .models import codepipeline_backends


class CodePipelineResponse(BaseResponse):
    @property
    def codepipeline_backend(self):
        return codepipeline_backends[self.region]

    def create_pipeline(self):
        pipeline, tags = self.codepipeline_backend.create_pipeline(
            self.region, self._get_param("pipeline"), self._get_param("tags")
        )

        return json.dumps({"pipeline": pipeline, "tags": tags})

    def get_pipeline(self):
        pipeline, metadata = self.codepipeline_backend.get_pipeline(
            self._get_param("name")
        )

        return json.dumps({"pipeline": pipeline, "metadata": metadata})
