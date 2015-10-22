# handling undefined values in bottle's SimpleTemplate Engine templates
{{thing['attr'] if defined('thing') else ''}}
