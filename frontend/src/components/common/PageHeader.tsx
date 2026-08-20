interface PageHeaderProps {
  title: string;
  description?: string;
}

function PageHeader({
  title,
  description,
}: PageHeaderProps) {
  return (
    <div className="page-header">

      <div>
        <h1>{title}</h1>

        {description && (
          <p>
            {description}
          </p>
        )}

      </div>

    </div>
  );
}

export default PageHeader;