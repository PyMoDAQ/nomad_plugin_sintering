from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class SinteringEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_plugin_sintering.schema_packages.sintering import m_package

        return m_package


sintering_entry_point = SinteringEntryPoint(
    name='Sintering',
    description='New schema for the Sintering process.',
)
