<nav class="navbar fixed-top navbar-expand-lg bg-primary" data-bs-theme="dark">
	<div class="container-fluid">
		<a class="navbar-brand" href="/">
			<img src="./favicon.png" alt="Logo" height="24" class="d-inline-block align-text-top" />
			SeSAC CRM
		</a>
		<button
			class="navbar-toggler"
			type="button"
			data-bs-toggle="collapse"
			data-bs-target="#navbarColor01"
			aria-controls="navbarColor01"
			aria-expanded="false"
			aria-label="Toggle navigation"
		>
			<span class="navbar-toggler-icon"></span>
		</button>
		<div class="collapse navbar-collapse" id="navbarColor01">
			<ul class="navbar-nav me-auto">
				<li class="nav-item">
					<a class="nav-link active" href="/"
						>Home
						<span class="visually-hidden">(current)</span>
					</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="/user">User</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="/store">Store</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="/item">Item</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="/order">Order</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="/orderitem">Order Item</a>
				</li>
			</ul>
			<div class="d-flex"></div>
		</div>
	</div>
</nav>

<div class="py-5">
	<div class="container py-4">
		<slot></slot>
	</div>
</div>

<nav class="navbar fixed-bottom bg-body-tertiary">
	<div class="container-fluid">
		<span class="navbar-text">Customer Relationship Management</span>
	</div>
</nav>
